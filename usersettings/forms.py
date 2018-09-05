from django import forms
from django.forms import ModelForm, TextInput, FileInput, BaseInlineFormSet
from .models import Stylista
from django.forms.models import modelformset_factory, inlineformset_factory
from landing.models import Client, Stylist
from django.contrib.auth.models import User as AccountUser


class BaseUserForm(ModelForm):

    class Meta:
        model = AccountUser
        fields = ('first_name', 'last_name')
        widgets = {

                    'first_name': TextInput(attrs={'class': 'form-control account-input'}),
                    'last_name': TextInput(attrs={'class': 'form-control account-input'})
        }


class BaseClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class UploadStoreFrontForm(ModelForm):

    class Meta:
        model = Stylista
        exclude = ['user']
        fields = ('store_front',)
        widgets = {

            'store_front': FileInput(attrs={'class': 'form-control input-upload d-inline'})

        }


class UpdateClientInfo(ModelForm):

    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control account-input'}),
                                 required=False)

    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control account-input'}),
                                required=False)

    class Meta:
        model = Stylista
        fields = ('address', 'zip_code', 'city', 'country', 'phone_number')
        field_order = ['zip_code', 'address', 'city', 'first_name', 'last_name', 'country', 'phone_number']
        widgets = {

                    'address': TextInput(attrs={'class': 'form-control account-input'}),
                    'zip_code': TextInput(attrs={'class': 'form-control account-input'}),
                    'city': TextInput(attrs={'class': 'form-control account-input'}),
                    'country': TextInput(attrs={'class': 'form-control account-input'}),
                    'phone_number': TextInput(attrs={'class': 'form-control account-input'}),

                }
