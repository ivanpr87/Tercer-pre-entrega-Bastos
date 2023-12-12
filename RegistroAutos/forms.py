from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Auto, Cliente, Perfil, CustomUser

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['fabricante', 'modelo', 'año', 'color', 'imagen']

    imagen = forms.ImageField(widget=forms.FileInput)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rol', 'avatar']

class CustomUserCreationForm(UserCreationForm):
    USUARIO_COMUN = 'comun'
    ADMINISTRADOR = 'admin'

    ROLES_CHOICES = [
        (USUARIO_COMUN, 'Usuario Común'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    rol = forms.ChoiceField(choices=ROLES_CHOICES)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'rol', 'avatar']


class BorrarAutoForm(forms.Form):
    auto_id = forms.ModelChoiceField(queryset=Auto.objects.all(), widget=forms.Select, empty_label=None)

class SeleccionarAutoForm(forms.Form):
    auto_id = forms.IntegerField()

class ModificarAutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['fabricante', 'modelo', 'año', 'color', 'imagen']




