from django.shortcuts import render
from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from usuario.models import  Usuario, Empresa
from usuario.serializers import UsuarioListSerializer, UsuarioSerializer, EmpresaSerializer, EmpresaListSerializer
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usuarios(request):
    usuarioList = Usuario.objects.all()
    usuario_serializer = UsuarioSerializer(usuarioList, many=True)
    return JsonResponse(usuario_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usuarios_list(request):
    usuarioList = Usuario.objects.all()
    UsuarioSerializer = UsuarioListSerializer

    usuario_serializer = UsuarioListSerializer(usuarioList, many=True)
    return JsonResponse(usuario_serializer.data, safe=False)

class UsuarioListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer
    search_fields = ['email']
    #filter_fields = ('first_name')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def empresa_list(request):
    if request.method == 'GET':
        empresaList = Empresa.objects.all()
        
        id = request.GET.get('id', None)
        if id is not None:
            empresaList = empresaList.filter(id__icontains=id)
        
        empresa_serializer = EmpresaListSerializer(empresaList, many=True)
        return JsonResponse(empresa_serializer.data, safe=False)

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def empresa(request):
    if request.method == 'GET':
        empresa = Empresa.objects.all()
        
        id = request.GET.get('id', None)
        if id is not None:
            empresa = empresa.filter(id__icontains=id)
        
        empresa_serializer = EmpresaSerializer(empresa, many=True)
        return JsonResponse(empresa_serializer.data, safe=False)
    elif request.method == 'POST':
        empresa = Empresa.objects.all()
        empresa_data = JSONParser().parse(request)
        empresa_serializer = EmpresaSerializer(data=empresa_data)
        if empresa_serializer.is_valid():
            empresa_serializer.save()
            return JsonResponse(empresa_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(empresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, email):
    usuario_data = JSONParser().parse(request)
    print(usuario_data)
    usuario = Usuario.objects.get(email=email)
    usuario_serializer = UsuarioListSerializer(usuario,data=usuario_data)
    if usuario_serializer.is_valid():
        usuario_serializer.save()
        return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

