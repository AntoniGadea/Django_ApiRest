from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.CharField(max_length=9, blank=False, primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=100, blank=False)
    token = models.CharField(max_length=100, blank=True, default='')
    creado = models.DateField(editable=False, auto_now=True)
    id_Empresa = models.CharField(max_length=9, blank=True, default='')
    ts = models.DateField()

class UsuarioList(models.Model):
    id = models.CharField(max_length=9, blank=False, primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=20, blank=False)
    ts = models.DateField()

class UsuarioLogin(models.Model):
    token = models.CharField(max_length=100, blank=False)