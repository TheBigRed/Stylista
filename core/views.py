from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('core/core.html')
    context = {}
    return HttpResponse(template.render(context, request))
