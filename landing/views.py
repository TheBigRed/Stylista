from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import Stylist
from datetime import datetime
from django.urls import reverse


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}
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


def name(request):
    """
    :param request: name
    :return: list of stylists in database
    """
    name_styl = Stylist.objects.order_by('-joined_date')
    return HttpResponse(name_styl)


def signup(request):
    """
    :param request: singup
    :return: form to signup for account
    """
    return render(request, 'landing/signup.html')


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
        #new_stylist.save()
        #return HttpResponseRedirect('landing:thankyou', args=(fullname,))
        return HttpResponseRedirect(reverse('landing:thankyou', args=(fullname,)))


def thankyou(request, fullname):
    """
    :param request: get full name of user who signed up
    :return: thank you for signing up page
    """
    return render(request, 'landing/thankyou.html', {'fullname': fullname})
