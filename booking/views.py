from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from core.models import Account, Gallery, Service
from landing.models import Stylist
from landing.utils import get_dbsession
from django.urls import reverse


def main(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    return HttpResponse("Booking Main")
