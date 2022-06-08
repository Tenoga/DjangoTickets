from dataclasses import fields
from django import forms
from .models import Pasajero

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'