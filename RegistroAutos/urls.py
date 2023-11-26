from django.urls import path
from .views import home, agregar_auto, ver_autos, register, cerrar_sesion, MiLoginView, ver_registros_actividades, agregar_cliente, ver_clientes
urlpatterns = [
    path('', home, name='home'),
    path('agregar_auto/', agregar_auto, name='agregar_auto'),
    path('ver_autos/', ver_autos, name='ver_autos'),
    path('register/', register, name='register'),
    path('logout/', cerrar_sesion, name='logout'),
    path('login/', MiLoginView.as_view(), name='login'),
    path('ver_registros_actividades/', ver_registros_actividades, name='ver_registros_actividades'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('ver_clientes/', ver_clientes, name='ver_clientes'),

]
