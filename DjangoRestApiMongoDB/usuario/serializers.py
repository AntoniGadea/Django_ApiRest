from rest_framework import serializers
from usuario.models import Usuario, Empresa, UsuarioList

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
                  'nombre',
                  'apellidos',
                  'email',
                  'password',
                  'groups',
                  'user_permissions',
                  'is_staff',
                  'is_active',
                  'is_superuser',
                  'last_login',
                  'date_joined',
                  'groups',
                  'registroTrabajo',
                  'img',
                  'settings',
                  'empresa'
                  )
        
class UsuarioListSerializer(serializers.ModelSerializer):
    registroTrabajo = serializers.JSONField()
    class Meta:
        model = Usuario
        fields = (
                  'email',
                  'nombre',
                  'apellidos',
                  'last_login',
                  'date_joined',
                  'registroTrabajo',
                  'img',
                  'settings',
                  'empresa'
                  )


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = (
            'id',
            'nombre',
            'email',
            'empleados',
            'creado',
            'ts',
            'img',
        )

class EmpresaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = (
            'id',
            'nombre',
            'email',
            'img',
        )

