#-*- encoding: utf-8 -*-
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from materia.models import datoshorario, horas, datosmateria
from usuario.models import datosusuario
from semestre.models import semestre, vacaciones
from .serializers import HoraSerializer, HorarioSerializer, MateriaSerializer, UsuarioSerializer, SemestreSerializer, VacacionesSerializer

#Recuerda importar todo lo que necesites.
#Vistas de la API de los datos del modelo "materia".
#view de la API del horario.
@api_view(['GET', 'POST'])

def horario_list(request):
    try:
        #La linea de abajo es cómo se hace una consulta a la base de datos
        horario_obj = datoshorario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = HorarioSerializer(horario_obj, many=True)
        return Response(serializer.data)

#view de la API de las horas. uwu
@api_view(['GET', 'POST'])

def hora_list(request):
    try:
        hora_obj = horas.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = HoraSerializer(hora_obj, many=True)
        return Response(serializer.data)

#View de la API de las materias.
@api_view(['GET', 'POST'])

def materia_list(request):
    try:
        materia_obj = datosmateria.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = MateriaSerializer(materia_obj, many=True)
        return Response(serializer.data)

#Vistas de la API de los datos del modelo "usuario".
#View de la API de los datos del usuario.
@api_view(['GET', 'POST'])

def usuario_list(request):
    try:
        usuario_obj = datosusuario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario_obj, many=True)
        return Response(serializer.data)

#Vistas de la API del modelo "semestre"
#View de la API de los datos del semestre
@api_view(['GET', 'POST'])

def semestre_list(request):
    try:
        semestre_obj = semestre.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = SemestreSerializer(semestre_obj, many=True)
        return Response(serializer.data)

#View de la API de los datos de las vacaciones
@api_view(['GET', 'POST'])
def vacaciones_list(request):
    try:
        vacaciones_obj = vacaciones.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = VacacionesSerializer(vacaciones_obj, many=True)
        return Response(serializer.data)
