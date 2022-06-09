from dataclasses import fields
from django import forms
from .models import Tiquetes

class TiqueteForm(forms.ModelForm):
    class Meta:
        model = Tiquetes
        fields = '__all__'