from django.urls import path
from .views import home, agregar_auto, ver_autos, register, cerrar_sesion, MiLoginView, ver_registros_actividades, agregar_cliente, ver_clientes, borrar_auto, modificar_auto, detalles_auto, about, pagina_no_encontrada


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
    path('modificar_auto/', modificar_auto, name='modificar_auto'),
    path('borrar_auto/', borrar_auto, name='borrar_auto'),
    path('detalles_auto/<int:auto_id>/', detalles_auto, name='detalles_auto'),
    path('about/', about, name='about'),
    path('404/', pagina_no_encontrada, name='404'),


]
handler404 = 'RegistroAutos.views.pagina_no_encontrada'

