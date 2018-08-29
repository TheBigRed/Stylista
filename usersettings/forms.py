from django import forms
from django.forms import ModelForm, FileInput
from .models import Stylista
from core.models import Account


# class UploadStoreFrontForm(ModelForm):
#
#     class Meta:
#         model = Stylista
#         exclude = ['user']
#         fields = ('store_front',)
#         # fields = ('store_front', 'first_name', 'last_name', 'password')
#         # #fields = ('store_front', 'first_name', 'last_name', 'password')
#         # widgets = {
#         #
#         #     'store_front': FileInput(attr={'class': 'form-control input-signup'})
#         #
#         # }


class UploadStoreFrontForm(ModelForm):

    class Meta:
        model = Account
        exclude = ['user']
        fields = ('store_front',)
        widgets = {

            'store_front': FileInput(attrs={'class': 'form-control input-signup'})

        }