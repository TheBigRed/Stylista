from django import forms
from django.forms import ModelForm, TextInput
from .models import Client
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    remember_me = forms.BooleanField(label='Remember me',
                                     widget=forms.CheckboxInput(attrs={'class': 'form-check form-check-inline '
                                                                                'kottai'}))

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control input-login'}),
            'password': TextInput(attrs={'class': 'form-control input-login'}),
        }


class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        widgets = {
            'email': TextInput(attrs={'class': 'form-control input-signup'}),
            'first_name': TextInput(attrs={'class': 'form-control input-signup'}),
            'last_name': TextInput(attrs={'class': 'form-control input-signup'}),
            'password': TextInput(attrs={'class': 'form-control input-signup'}),
        }