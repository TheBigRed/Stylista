from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from core.models import Account, Gallery
from landing.models import Stylist
from .forms import UploadFileForm
from landing.utils import get_dbsession
from django.urls import reverse


def main(request):
    '''
    :param request: get request which has user on db session stored in session cookie
    :return: main page with correct user after authenticate session
    '''
    if request.session.keys():
        s = get_dbsession(request.session['session_login'])
        stylist = Stylist.objects.get(pk=s['user_pk'])
        accounts = Account.objects.filter(stylist_type='BARBER')

        print("Received cookie session: {}".format(request.session.session_key))
        request.session.cycle_key()
        #print("Main page received user session: {0}".format(user_session))
        #print("New cookie session {0} with db session value {1}".format(request.session.session_key, request.session['session_login']))
        return render(request, 'core/main.html', {'stylist': stylist, 'accounts': accounts})
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


def uploadmodule(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            s = get_dbsession(request.session['session_login'])
            edit_account = Account.objects.get(account_holder_id=int(s['user_pk']))
            edit_account.store_front = form.cleaned_data['file']
            edit_account.save()
            return HttpResponse("Uploaded <filename>")
    else:
        form = UploadFileForm()
        return render(request, 'core/upload_module.html', {'uploadform': form})
    return render(request, 'core/upload_module.html', {})


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
        print("Store name : " + store_front)
        s = get_dbsession(request.session['session_login'])
        stylist = Stylist.objects.get(pk=s['user_pk'])
        print("User Session: {}".format(stylist.first_name))
        account = Account.objects.get(store_name=store_front)
        gallery_imgs = Gallery.objects.filter(user_id=account.account_holder_id)

        for imgs in gallery_imgs:
            print(imgs.picture)
            print(imgs.caption)
            print(imgs.picture.url)

        request.session.cycle_key()
        return render(request, 'core/profile.html', {'account': account, 'imgs': gallery_imgs})

    else:
        return HttpResponseRedirect(reverse('landing:login'))
