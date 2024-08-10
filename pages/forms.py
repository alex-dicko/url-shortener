from django.forms import ModelForm
from django import forms
from . models import link
from django.utils.safestring import mark_safe
 

class LinkForm(ModelForm):
    class Meta:
        model = link
        fields = ['redirect_link']
    
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['redirect_link'].widget.attrs['placeholder'] = mark_safe('Enter Link Here')