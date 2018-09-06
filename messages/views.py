from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from landing.models import Stylist, Client
from django.urls import reverse
from core.models import Account
from django.contrib.auth.models import User


def messages(request):
    return HttpResponse("Messaging App")