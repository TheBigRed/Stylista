from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.template import loader
from django.shortcuts import render, redirect
from .models import Stylist
from datetime import datetime
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from core.models import Account
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from landing.utils import create_session
from django.contrib.sessions.backends.db import SessionStore


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}

    user_client = User.objects.get(username='test_user')
    client_address = user_client.client.address
    print("User name {}".format(user_client.first_name + user_client.last_name))
    print("User address {}".format(client_address))

    return HttpResponse(template.render(context, request))


def stylist(request, stylist_id):
    """
    :param request: stylist pk
    :return: Stylist object
    """
    try:
        stylist_obj = Stylist.objects.get(pk=stylist_id)
    except Stylist.DoesNotExist:
        raise Http404("Stylist does not exist")
    return render(request, 'landing/stylist.html', {'stylist': stylist_obj})


def signup(request):
    """
    :param request: singup
    :return: form to signup for account
    """
    form = SignUpForm()
    context = {

        'form': form

    }

    return render(request, 'landing/signup.html', context)


def newuser(request):
    """
    :param request: receive form data
    :return: redirect to thank you page
    """
    try:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        fullname = firstname + " " + lastname
    except KeyError:
        raise Http404("Please sign up")
    else:
        new_stylist = Stylist()
        new_stylist.first_name = firstname
        new_stylist.last_name = lastname
        new_stylist.email = email
        new_stylist.password = password
        new_stylist.joined_date = datetime.now()
        new_stylist.save()

        new_account = Account.objects.create(account_holder=new_stylist)
        new_account.save()

        return HttpResponseRedirect(reverse('landing:thankyou', args=(fullname,)))


def login(request):
    """
    :param request: none
    :return: about site page
    """
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = "form-control input-login"
    form.fields['password'].widget.attrs['class'] = "form-control input-login"

    context = {

        'form': form

    }

    return render(request, 'landing/login.html', context)


def authentication(request):
    """
    :param request: receive form data login
    :return: redirect to page main page after login
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                print("Logged in: " + user.__str__())
                auth_login(request, user)
                #create_session(request, 10)
                return HttpResponseRedirect(reverse('core:main'))

            else:
                return HttpResponse("Invalid Username or Password")

        else:
            print("error: {}".format(form.errors))
            print(form.errors.as_data())
            print("FORM INVALID")
            form.fields['username'].widget.attrs['class'] = "form-control input-login"
            form.fields['password'].widget.attrs['class'] = "form-control input-login"
            return render(request, 'landing/login.html', {'form': form})
            #return HttpResponseRedirect(reverse('core:main'))

    form = AuthenticationForm()
    return render(request, 'landing/login.html', {'form': form})


def account(request, kottai):
    """
    :param request: get full name of user who signed up
    :return: thank you for signing up page
    """
    return render(request, 'landing/account.html', {'email': kottai})


def thankyou(request):
    """
    :param request: get full name of user who signed up
    :return: thank you for signing up page
    """
    return render(request, 'landing/thankyou.html')


def about(request):
    """
    :param request: none
    :return: about site page
    """
    return render(request, 'landing/about.html')
