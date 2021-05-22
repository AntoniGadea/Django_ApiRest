from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from usuario.models import UsuarioList, UsuarioLogin, Usuario
from usuario.serializers import UsuarioListSerializer, UsuarioSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def usuario_list(request):
    if request.method == 'GET':
        usuarioList = Usuario.objects.all()
        
        id = request.GET.get('id', None)
        if id is not None:
            usuarioList = usuarioList.filter(id__icontains=id)
        
        usuario_serializer = UsuarioListSerializer(usuarioList, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)
    elif request.method == 'POST':
        usuario = Usuario.objects.all()
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)