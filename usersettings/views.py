from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from landing.utils import get_dbsession
from django.urls import reverse
from django.views import View
from landing.models import Stylist, Stylista, Client
from core.models import Account
from .forms import UploadStoreFrontForm, UpdateClientInfo


def index(request):
    client = Client.objects.get(pk=2)
    form = UpdateClientInfo(instance=client)
    context = {

        'form': form

    }

    return render(request, 'usersettings/settings.html', context)
    # if request.session.keys():
    #     s = get_dbsession(request.session['session_login'])
    #     stylist = Stylist.objects.get(pk=s['user_pk'])
    #     print("Received cookie session: {}".format(stylist.first_name))
    #     return render(request, 'usersettings/settings.html', {'stylist': stylist})
    #
    # else:
    #     return HttpResponseRedirect(reverse('landing:login'))


def updateaccount(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    if request.method == 'POST':
        client = Client.objects.get(pk=2)
        form = UpdateClientInfo(instance=client, data=request.POST)

        if form.is_valid():
            #form.save(commit=False)
            first_name = client.user.first_name
            print("Client Name: {}".format(first_name))
            # print("Account Holder: {}".format(form.instance.user))
            # print("Account Store Front: {}".format(form.instance.store_front))
            # form.save()
            return HttpResponse("ACCOUNT UPDATED")

        else:
            print("error: {}".format(form.errors))
            print(form.errors.as_data())
            return render(request, 'usersettings/settings.html', {'form': form})
            return HttpResponse("FORM INVALID")

    return HttpResponseRedirect(reverse("usersettings:index"))
    # if request.session.keys():
    #     s = get_dbsession(request.session['session_login'])
    #     stylist = Stylist.objects.get(pk=s['user_pk'])
    #     account = Account.objects.get(account_holder_id=s['user_pk'])
    #
    #     print("Received cookie session: {}".format(request.session.session_key))
    #     print("Update session for : {}".format(stylist.first_name))
    #     print("Account session for: {}".format(account.account_holder))
    #     request.session.cycle_key()
    #
    #     try:
    #         firstname = request.POST['firstname']
    #         lastname = request.POST['lastname']
    #         #email = request.POST['email']
    #         #password = request.POST['password']
    #         phone_number = request.POST['phone_number']
    #         gender = request.POST['gender']
    #         stylist_type = request.POST['stylist_type']
    #         print("Retreived phone number value : {}".format(phone_number))
    #         Account.objects.filter(pk=account.pk).update(phone_number=phone_number,
    #                                                      gender=gender,
    #                                                      stylist_type=stylist_type)
    #
    #         return render(request, 'usersettings/settingupdated.html', {'stylist': stylist})
    #
    #     except KeyError:
    #         raise Http404("Please sign up")
    #
    # else:
    #     return HttpResponseRedirect(reverse('landing:login'))


def img_upload(request):
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         s = get_dbsession(request.session['session_login'])
    #         edit_account = Account.objects.get(account_holder_id=int(s['user_pk']))
    #         edit_account.store_front = form.cleaned_data['file']
    #         edit_account.save()
    #         return HttpResponse("Uploaded <filename>")
    # else:
    #     form = UploadFileForm()
    #     return render(request, 'core/upload_module.html', {'uploadform': form})
    account = Account.objects.get(pk=20)
    form = UploadStoreFrontForm()
    context = {

        'form': form

    }

    return render(request, 'usersettings/img_upload.html', context)


def uploaded(request):

    if request.method == 'POST':
        stylista = Stylista.objects.get(pk=4)
        form = UploadStoreFrontForm(instance=stylista, data=request.POST, files=request.FILES)

        if form.is_valid():

            if len(request.FILES) != 0:
                print("FORM VALIDATED")
                form.save(commit=False)
                file = request.FILES['store_front'].name
                print("File Name: {}".format(file))
                print("Account Holder: {}".format(form.instance.user))
                print("Account Store Front: {}".format(form.instance.store_front))
                form.save()
                return HttpResponse("Form VALID")

            else:
                return HttpResponseRedirect(reverse("usersettings:img_upload"))

        else:
            print(form.errors)
            return HttpResponse("Form INVALID")

    return HttpResponseRedirect(reverse("usersettings:img_upload"))

