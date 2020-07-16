from django.forms import CharField, ModelForm, TextInput
from django import forms

from Coming.models import Email

class ServerForm(ModelForm):

    class Meta:
        model = Email
        fields = ['email']
        widgets = {
            'email': TextInput(attrs={'class': 'form-control-lg form-control'}),
            }