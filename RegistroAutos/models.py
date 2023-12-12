from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, Permission, Group

class MarcaAuto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    color = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)

    def __str__(self):
        return f'{self.fabricante} - {self.modelo} - {self.año}'

    def get_imagen_url(self):
        if self.imagen:
            return self.imagen.url
        return None

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # Ejemplo: 'Agregar Auto'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.activity_type}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Perfil(models.Model):
    USUARIO_COMUN = 'comun'
    ADMINISTRADOR = 'admin'

    ROLES_CHOICES = [
        (USUARIO_COMUN, 'Usuario Común'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=ROLES_CHOICES, default=USUARIO_COMUN)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.rol}'

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
class CustomUser(AbstractUser):
    USUARIO_COMUN = 'comun'
    ADMINISTRADOR = 'admin'

    ROLES_CHOICES = [
        (USUARIO_COMUN, 'Usuario Común'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=ROLES_CHOICES, default=USUARIO_COMUN)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions', blank=True)

    def __str__(self):
        return self.username