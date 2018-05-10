from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from core.models import Account
from landing.models import Stylist
from .forms import UploadFileForm


def main(request, stylist):
    template = loader.get_template('core/main.html')
    context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'core/main.html', {'stylist': stylist})


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

    template = loader.get_template('core/main.html')
    context = {}
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
            fs = FileSystemStorage()
            aa = Account(account_holder_id=8, store_front=form.cleaned_data['file'])
            aa.save()
            fs.save(form.cleaned_data['title'] + 'fs', form.cleaned_data['file'], max_length=4000)
            return HttpResponse("Uploaded <filename>")
    else:
        form = UploadFileForm()
        return render(request, 'core/upload_module.html', {'uploadform': form})
    return render(request, 'core/upload_module.html', {})
