from rest_framework import serializers
from materia.models import datoshorario, datosmateria, horas
from usuario.models import datosusuario
from examen.models import examen, alarmaexamen, repeticionexamen
from semestre.models import semestre, vacaciones
from tarea .models import tarea,alarmatarea, repeticionalarma

#Admin = dinosaurio pass= dino1234

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = horas
        fields = '__all__'

# class MateriaSerializer(serializers.ModelSerializer):
#     horas = HoraSerializer(many=True)
#     class Meta:
#         model = datosmateria
#         fields = ('id','materia','profesor','horario','horas')

class HorarioSerializer(serializers.ModelSerializer):
    #materias = MateriaSerializer(many=True)
    class Meta:
        model = datoshorario
        fields = ('user', 'semestre')
        depth = 1

"""class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model ="""
