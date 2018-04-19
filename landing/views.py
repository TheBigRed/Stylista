from django.http import HttpResponse
from .models import Stylist


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, stylist_id):
    return HttpResponse("You're looking at question %s." % stylist_id)


def name(request):
    name_styl = Stylist.objects.order_by('-joined_date')
    return HttpResponse(name_styl)
