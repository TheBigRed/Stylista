from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Stylist


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def detail(request, stylist_id):
    try:
        stylist_name = Stylist.objects.get(pk=stylist_id)
    except Stylist.DoesNotExist:
        raise Http404("Stylist does not exist")
    return render(request, 'landing/detail.html', {'stylist': stylist_name})


def name(request):
    name_styl = Stylist.objects.order_by('-joined_date')
    return HttpResponse(name_styl)
