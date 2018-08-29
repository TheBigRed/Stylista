from django import forms
from django.forms import ModelForm
from .models import Stylista


class UploadStoreFrontForm(ModelForm):

    class Meta:
        model = Stylista
        exclude = ['user']
        fields = ('store_front',)
        # fields = ('store_front', 'first_name', 'last_name', 'password')
        # #fields = ('store_front', 'first_name', 'last_name', 'password')
        # widgets = {
        #
        #     'store_front': FileInput(attr={'class': 'form-control input-signup'})
        #
        # }
