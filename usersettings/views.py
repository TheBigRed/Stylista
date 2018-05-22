from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from landing.utils import get_dbsession
from django.urls import reverse
from landing.models import Stylist
from core.models import Account


def index(request):

    if request.session.keys():
        s = get_dbsession(request.session['session_login'])
        stylist = Stylist.objects.get(pk=s['user_pk'])
        print("Received cookie session: {}".format(stylist.first_name))
        return render(request, 'usersettings/settings.html', {'stylist': stylist})

    else:
        return HttpResponseRedirect(reverse('landing:login'))


def updateaccount(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    if request.session.keys():
        s = get_dbsession(request.session['session_login'])
        stylist = Stylist.objects.get(pk=s['user_pk'])
        account = Account.objects.get(account_holder_id=s['user_pk'])
        Account.objects.filter(pk=account.pk).update(address='updated')
        print("Received cookie session: {}".format(request.session.session_key))
        print("Update session for : {}".format(stylist.first_name))
        print("Account session for: {}".format(account.account_holder))
        request.session.cycle_key()

        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            # email = request.POST['email']
            # password = request.POST['password']
            # phone_number = request.POST['phone_number']
            # gender = request.POST['gender']
            # stylist_type = request.POST['stylist_type']

            print("Retrieved from post firstname: {}".format(firstname))
            return HttpResponse("Updated account")

        except KeyError:
            raise Http404("Please sign up")



    else:
        return HttpResponseRedirect(reverse('landing:login'))