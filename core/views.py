from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from core.models import Account
from landing.models import Stylista, Stylist
from landing.utils import get_dbsession
from django.urls import reverse


def main(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    if request.user.is_authenticated:
        print("Authorizing access for: " + request.user.username)
        context = {

            'user': request.user

        }

        return render(request, 'core/main.html', context)

    else:
        return HttpResponseRedirect(reverse('landing:login'))


def searchresults(request):
    try:
        search = request.GET['search']
        location = request.GET['location']
        result_list = Stylist.objects.filter(first_name__icontains=search)
        #result_lists = ', '.join([q.first_name for q in result_list])
        result_lists = list(result_list)
        if not result_list:
            return HttpResponse("No results found")
        else:
            return render(request, 'core/results.html', {'results': result_lists, 'size': len(result_lists)})

    except KeyError:
        return HttpResponse("Does not Exist")

    #template = loader.get_template('core/main.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    #return render(request, 'core/main.html', {'stylist': stylist})


def searchrefined(request):
    template = loader.get_template('core/main.html')
    context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'core/refined.html')





def stylistsearchmodule(request):
    # print(request.build_absolute_uri('?'))
    # print(request.build_absolute_uri())
    try:
        search = request.GET['btnValue1']
        print("Search value: " + search)
        accounts = Account.objects.filter(stylist_type=search)
        print("Returned : {}".format(accounts))
        return render(request, 'core/refined.html', {"accounts": accounts})
    except KeyError:
        return HttpResponse("Does not Exist")


def profile(request, store_front):
    if request.session.keys():
        client_session = get_dbsession(request.session['session_login'])
        stylist = Stylist.objects.get(pk=client_session['user_pk'])
        account = Account.objects.get(store_name=store_front)
        request.session.cycle_key()
        return render(request, 'core/profile.html', {'account': account})

    else:
        return HttpResponseRedirect(reverse('landing:login'))


def test_bench(request):
    stylista = Stylista.objects.get(pk=4)
    stylista.change_service_value('BJ', '1000')
    stylista.save()
    # print(stylista.user)
    # print(stylista.business_name)
    # j = json.dumps(stylista.services, indent=4, sort_keys=True)
    # loaded_j = json.loads(j)
    # print("JSON: {}".format(j))
    # loaded_j['BJ'] = '40'
    # print("Changed JSON: {}".format(json.dumps(loaded_j, indent=4, sort_keys=True)))
    # stylista.services = loaded_j
    # stylista.save()

    return HttpResponse("This is a test bench")
