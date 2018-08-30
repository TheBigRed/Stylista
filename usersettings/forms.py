from django import forms
from django.forms import ModelForm, FileInput
from .models import Stylista


class UploadStoreFrontForm(ModelForm):

    class Meta:
        model = Stylista
        exclude = ['user']
        fields = ('store_front',)
        widgets = {

            'store_front': FileInput(attrs={'class': 'form-control input-upload d-inline'})

        }
