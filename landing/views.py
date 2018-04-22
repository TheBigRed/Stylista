from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Stylist


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def stylist(request, stylist_id):
    """
    Returns stylist name based on primary key sent in
    & raises error if stylist doesn't exist
    """
    try:
        stylist_name = Stylist.objects.get(pk=stylist_id)
    except Stylist.DoesNotExist:
        raise Http404("Stylist does not exist")
    return render(request, 'landing/stylist.html', {'stylist': stylist_name})


def name(request):
    """
    :param request: name
    :return: list of stylists in database
    """
    name_styl = Stylist.objects.order_by('-joined_date')
    return HttpResponse(name_styl)
