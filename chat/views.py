from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from landing.models import Stylist, Client
from django.urls import reverse
from .models import Message, Conversation
from django.contrib.auth.models import User


def messages(request):

    if request.user.is_authenticated:
        print("Authorizing messages access for: " + request.user.username)
        print("Message user ID: " + str(request.user.pk))
        convo = Conversation.objects.get(sender=request.user.pk)
        print("Convo received for: " + str(convo))
        convo_messages = Message.objects.filter(conversation=convo.pk)
        context = {

            'messages': convo_messages,
            'current_user': str(request.user.username)

        }

        for m in convo_messages:
            if str(m.sender) == str(request.user.username):
                print("SENT: {}".format(m.message))
            else:
                print("RECEIVED: {}".format(m.message))

        return render(request, 'chat/messages.html', context)

    else:
        return HttpResponseRedirect(reverse('landing:login'))
