#-*- encoding: utf-8 -*-
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from materia.models import datoshorario, horas, datosmateria
from usuario.models import datosusuario
from semestre.models import semestre, vacaciones
from examen.models import examen, alarmaexamen, repeticionexamen
from tarea .models import tarea, alarmatarea, repeticiontarea
from .serializers import *

#Recuerda importar todo lo que necesites.
#Vistas de la API de los datos de la app "materia".
@api_view(['GET', 'POST'])

def horario_list(request):
    try:
        horario = datoshorario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = HorarioSerializer(horario, many=True)
        return Response(serializer.data)

#Vistas de la API de los datos de la app "usuario".
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

#Vistas de la API de la app "semestre"
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

#Vistas de la API de la app "examen"
#View de la API de los datos de examen
@api_view(['GET', 'POST'])

def examen_list(request):
    try:
        examen_obj = examen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = ExamenSerializer(examen_obj, many=True)
        return Response(serializer.data)

#View de la API de las alarmas de examenes
@api_view(['GET', 'POST'])

def alarmaexamen_list(request):
    try:
        alarmaexamen_obj = alarmaexamen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = AlarmaExamenSerializer(alarmaexamen_obj, many=True)
        return Response(serializer.data)

#View de la API de la repeticion de las alarmas
@api_view(['GET', 'POST'])

def repeticionalarmaexamen_list(request):
    try:
        repeticionalarmaexamen_obj = repeticionalarmaexamen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = RepeticionAlarmaExamenSerializer(repeticionalarmaexamen_obj, many=True)
        return Response(serializer.data)

#Vistas de la API de la app "tarea"
#View de la API de los datos de tarea
@api_view(['GET', 'POST'])

def tarea_list(request):
    try:
        tarea_obj = tarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = TareaSerializer(tarea_obj, many=True)
        return Response(serializer.data)

#View de la API de las alarmas de tareas
@api_view(['GET', 'POST'])

def alarmatarea_list(request):
    try:
        alarmatarea_obj = alarmatarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = AlarmaTareaSerializer(alarmatarea_obj, many=True)
        return Response(serializer.data)

#View de la API de la repeticion de las alarmas
@api_view(['GET', 'POST'])

def repeticionalarmatarea_list(request):
    try:
        repeticionalarmatarea_obj = repeticionalarmatarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = RepeticionAlarmaTareaSerializer(repeticionalarmatarea_obj, many=True)
        return Response(serializer.data)
