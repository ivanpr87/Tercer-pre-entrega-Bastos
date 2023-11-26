from django.shortcuts import render, redirect
from .models import Auto, UserActivity, Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from .forms import AutoForm, ClienteForm

def home(request):
    return render(request, 'home.html')



@login_required(login_url='login')
def agregar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            fabricante = form.cleaned_data['fabricante']
            modelo = form.cleaned_data['modelo']
            año = form.cleaned_data['año']
            color = form.cleaned_data['color']

            # Guarda la instancia de Auto
            auto = Auto.objects.create(
                fabricante=fabricante,
                modelo=modelo,
                año=año,
                color=color,
            )

            # Registra la actividad después de agregar un auto
            UserActivity.objects.create(user=request.user, activity_type='Agregar Auto')

            return redirect('ver_autos')
    else:
        form = AutoForm()

    return render(request, 'agregar_auto.html', {'form': form})

def ver_autos(request):
    query = request.GET.get('query', '')
    autos = Auto.objects.filter(modelo__icontains=query)
    return render(request, 'ver_autos.html', {'autos': autos, 'query': query})

def cerrar_sesion(request):
    logout(request)
    return render(request, 'logout.html')

class MiLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('nombre_de_la_pagina_de_inicio')

def ver_registros_actividades(request):
    user_activities = UserActivity.objects.all()
    return render(request, 'user_activity_list.html', {'user_activities': user_activities})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Ajusta según tu estructura de URL
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes agregar actividades, redirecciones, etc.
            return redirect('ver_clientes')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ver_clientes.html', {'clientes': clientes})

