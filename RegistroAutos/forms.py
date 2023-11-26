from django import forms
from .models import Auto, Cliente

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['fabricante', 'modelo', 'año', 'color']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion']

