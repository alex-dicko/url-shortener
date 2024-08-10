from django.forms import ModelForm
from django import forms
from . models import link

class LinkForm(ModelForm):
    class Meta:
        model = link
        fields = ['redirect_link']