from dataclasses import fields
from django import forms
from .models import Tiquetes

class TiqueteForm(forms.ModelForm):
    class Meta:
        model = Tiquetes
        fields = '__all__'
        widgets = {
            'ruta': forms.Select(attrs={
                'class': "form-control",
                'placeholder': "Seleccione su ruta"
                }),
            'bus': forms.Select(attrs={
                'class': "form-control", 
                'placeholder': 'Cootransfusa'
                }),
            'pasajero': forms.Select(attrs={
                'class': "form-control", 
                'placeholder': 'Pepito Perez'
                }),
            'cantidad': forms.NumberInput(attrs={
                'class': "form-control", 
                'placeholder': '2'
                }),
            'fecha_viaje': forms.TextInput(attrs={
                'class': "form-control",
                'onfocus': "(this.type='date')",
                'onblur': "(this.type='text')"
                }),
            'hora_salida': forms.TextInput(attrs={
                'class': "form-control",
                'onfocus': "(this.type='time')",
                'onblur': "(this.type='text')"
                })
        }