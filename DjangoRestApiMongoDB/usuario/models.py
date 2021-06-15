from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField
from usuario.managers import UsuarioManager

# Create your models here.
class Usuario(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()
    registroTrabajo = JSONField(null=False, blank=False, default={
        "horasTrabajadas":0,
        "ubicaciones": [],
        "vacacionesDisponibles":0,
        "vacacionesUsadas":0
    })
    settings = JSONField(null=True, blank=True)
    img = models.CharField(max_length=3000, blank=True, default='')
    empresa = models.CharField(max_length=30, blank=True, default='')
    nombre =  models.CharField(max_length=30, blank=True, default='')
    apellidos =  models.CharField(max_length=30, blank=True, default='')

class UsuarioList(models.Model):
    email = models.CharField(max_length=100)

class Empresa(models.Model):
    id = models.CharField(max_length=9, blank=False, primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=True, default='')
    empleados = JSONField(null=True)
    creado = models.DateField(editable=False, auto_now=True)
    ts = models.DateField()
    img = models.CharField(max_length=3000, blank=True, default='')

