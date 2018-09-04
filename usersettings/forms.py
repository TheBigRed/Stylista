from django import forms
from django.forms import ModelForm, TextInput, FileInput
from .models import Stylista


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
        field_order = ['first_name', 'last_name', 'address', 'zip_code', 'city', 'country', 'phone_number']
        widgets = {

                    'address': TextInput(attrs={'class': 'form-control account-input'}),
                    'zip_code': TextInput(attrs={'class': 'form-control account-input'}),
                    'city': TextInput(attrs={'class': 'form-control account-input'}),
                    'country': TextInput(attrs={'class': 'form-control account-input'}),
                    'phone_number': TextInput(attrs={'class': 'form-control account-input'}),

                }
