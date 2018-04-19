from django.http import HttpResponse
from django.template import loader
from .models import Stylist


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def detail(request, stylist_id):
    return HttpResponse("You're looking at question %s." % stylist_id)


def name(request):
    name_styl = Stylist.objects.order_by('-joined_date')
    return HttpResponse(name_styl)
