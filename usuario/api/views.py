#-*- encoding: utf-8 -*-
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from materia.models import datoshorario
from .serializers import HorarioSerializer

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
