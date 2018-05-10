from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label='title')
    file = forms.FileField(label='file')
