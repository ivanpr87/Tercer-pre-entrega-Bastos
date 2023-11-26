from django.db import models
from django.contrib.auth.models import User

class MarcaAuto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.modelo} - {self.año}'


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # Ejemplo: 'Agregar Auto', 'Ver Auto'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.activity_type}'

    from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
