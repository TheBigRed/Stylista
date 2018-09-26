from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from landing.models import Stylist, Client
from django.urls import reverse
from .models import Message
from django.contrib.auth.models import User


def messages(request):
    messagess = Message.objects.all()

    context = {

        'messages': messagess

    }

    for m in messagess:
        print(m.sender)
        print(m.message)

    return render(request, 'chat/messages.html', context)
