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


@api_view(['GET', 'POST'])
def horario_list(request):
    """API de materias
    vista API (app datos horario)
    """
    try:
        horario = datoshorario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = HorarioSerializer(horario, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def usuario_list(request):
    """API datos usuario
    vista API(app usuario)
    """
    try:
        usuario_obj = datosusuario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def semestre_list(request):
    """API de semestre
    vista API (app semestre)
    """
    try:
        semestre_obj = semestre.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = SemestreSerializer(semestre_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def vacaciones_list(request):
    """API de vacaciones
    vista API (app semestre)
    """
    try:
        vacaciones_obj = vacaciones.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = VacacionesSerializer(vacaciones_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def examen_list(request):
    """API de examenes
    vista API (app examen)
    """
    try:
        examen_obj = examen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = ExamenSerializer(examen_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def alarmaexamen_list(request):
    """API de alarma de examenes
    vista API (app examen)
    """
    try:
        alarmaexamen_obj = alarmaexamen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = AlarmaExamenSerializer(alarmaexamen_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def repeticionalarmaexamen_list(request):
    """API de hora de alarma de examenes
    vista API (app examen)
    """
    try:
        repeticionalarmaexamen_obj = repeticionalarmaexamen.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = RepeticionAlarmaExamenSerializer(
            repeticionalarmaexamen_obj,
            many=True
            )
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def tarea_list(request):
    """API de tareas
    vista API (app tarea)
    """
    try:
        tarea_obj = tarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = TareaSerializer(tarea_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def alarmatarea_list(request):
    """API de hora de alarma tarea
    vista API (app tarea)
    """
    try:
        alarmatarea_obj = alarmatarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = AlarmaTareaSerializer(alarmatarea_obj, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def repeticionalarmatarea_list(request):
    """API repeticion hora de alarma tarea
    vista API (app tarea)
    """
    try:
        repeticionalarmatarea_obj = repeticionalarmatarea.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = RepeticionAlarmaTareaSerializer(
            repeticionalarmatarea_obj,
            many=True
            )
        return Response(serializer.data)
