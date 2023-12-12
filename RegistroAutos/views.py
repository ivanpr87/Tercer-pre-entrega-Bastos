from django.shortcuts import render, redirect,get_object_or_404
from .models import Auto, UserActivity, Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from .forms import AutoForm, ClienteForm, PerfilForm, ModificarAutoForm, BorrarAutoForm, SeleccionarAutoForm
from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def agregar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            fabricante = form.cleaned_data['fabricante']
            modelo = form.cleaned_data['modelo']
            año = form.cleaned_data['año']
            color = form.cleaned_data['color']
            imagen = form.cleaned_data['imagen']

            # Utiliza get_or_create para evitar duplicados
            auto, created = Auto.objects.get_or_create(
                fabricante=fabricante,
                modelo=modelo,
                año=año,
                color=color,
                imagen=imagen,
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
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

class MiLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('home')

def ver_registros_actividades(request):
    user_activities = UserActivity.objects.all()
    return render(request, 'user_activity_list.html', {'user_activities': user_activities})

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        perfil_form = PerfilForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'perfil_form': perfil_form})



@login_required(login_url='login')
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ver_clientes.html', {'clientes': clientes})

@user_passes_test(lambda u: u.perfil.rol == 'admin', login_url='home')
@login_required(login_url='login')
def modificar_auto(request):
    autos = Auto.objects.all()

    if request.method == 'POST':
        seleccionar_auto_form = SeleccionarAutoForm(request.POST)

        if seleccionar_auto_form.is_valid():
            auto_id = seleccionar_auto_form.cleaned_data['auto_id']

            try:
                auto = Auto.objects.get(id=auto_id)
            except Auto.DoesNotExist:
                # Si el auto no existe, mostrar un mensaje de error y redirigir a alguna página
                return render(request, 'auto_no_encontrado.html', {'auto_id': auto_id})

            modificar_auto_form = ModificarAutoForm(request.POST, request.FILES, instance=auto)

            if modificar_auto_form.is_valid():
                modificar_auto_form.save()
                return redirect('ver_autos')

    else:
        seleccionar_auto_form = SeleccionarAutoForm()
        modificar_auto_form = None

    return render(request, 'modificar_auto.html', {'seleccionar_auto_form': seleccionar_auto_form, 'modificar_auto_form': modificar_auto_form})


@user_passes_test(lambda u: u.perfil.rol == 'admin', login_url='home')
@login_required(login_url='login')
def borrar_auto(request):
    autos = Auto.objects.all()

    if request.method == 'POST':
        form = BorrarAutoForm(request.POST)
        if form.is_valid():
            try:
                auto = form.cleaned_data['auto_id']
                if auto:
                    auto.delete()
                    print(f"Auto ID {auto.id} borrado correctamente")
                    # Registrar actividad después de borrar el auto
                    UserActivity.objects.create(user=request.user, activity_type='Borrar Auto')
                    return redirect('ver_autos')
            except Exception as e:
                print(f"Error al borrar el auto: {e}")
    else:
        form = BorrarAutoForm()

    return render(request, 'borrar_auto.html', {'form': form, 'autos': autos})

def detalles_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    return render(request, 'detalles_auto.html', {'auto': auto})



def about(request):
    return render(request, 'about.html')

def pagina_no_encontrada(request, exception=None):
    return render(request, 'auto_no_encontrado.html', status=404)