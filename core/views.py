from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from landing.models import Stylist


def main(request, stylist):
    template = loader.get_template('core/main.html')
    context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'core/main.html', {'stylist': stylist})


def searchresults(request):
    try:
        search = request.GET['search']
        location = request.GET['location']
        return render(request, 'core/results.html', {'search': search})

    except KeyError:
        return HttpResponse("Does not Exist")

    template = loader.get_template('core/main.html')
    context = {}
    #return HttpResponse(template.render(context, request))
    #return render(request, 'core/main.html', {'stylist': stylist})