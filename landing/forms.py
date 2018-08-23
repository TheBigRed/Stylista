from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User


class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control input-login'}),
            'password': TextInput(attrs={'class': 'form-control input-login'}),
        }