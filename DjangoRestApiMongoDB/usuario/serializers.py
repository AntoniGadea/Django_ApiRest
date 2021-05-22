from rest_framework import serializers
from usuario.models import UsuarioList, Usuario
from usuario.models import UsuarioLogin

class UsuarioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioList
        fields = ('id',
                  'nombre',
                  'apellido',
                  'ts')

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id',
                  'nombre',
                  'apellido',
                  'password',
                  'token',
                  'creado',
                  'id_Empresa',
                  'ts',
                  )