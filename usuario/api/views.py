#-*- encoding: utf-8 -*-
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from materia.models import datoshorario
from .serializers import HoraSerializer, HorarioSerializer#, MateriaSerializer
from materia.models import horas

#API del horario pero era para una version antigua y ya no sirve xD
@api_view(['GET', 'POST'])

def horario_list(request):
    try:
        horario_obj = datoshorario.objects.all()
    except Exception as e:
        print(e)
        print(type(e))
    if request.method == 'GET':
        serializer = HorarioSerializer(horario_obj, many=True)
        return Response(serializer.data)

#API de las horas uwu
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

#API de
