from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from landing.utils import get_dbsession
from django.urls import reverse
from landing.models import Stylist
from core.models import Account


def index(request):
    return render(request, 'usersettings/settings.html')


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

        return HttpResponse("Updated account")
    else:
        return HttpResponseRedirect(reverse('landing:login'))