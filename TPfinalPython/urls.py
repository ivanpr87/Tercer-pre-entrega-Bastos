# En tu archivo urls.py principal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RegistroAutos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
