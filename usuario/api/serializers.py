from rest_framework import serializers
from materia.models import datoshorario, datosmateria, horas
from ..models import datosusuario
from examen.models import examen, alarmaexamen, repeticionexamen
from semestre.models import semestre, vacaciones
from tarea .models import tarea,alarmatarea, repeticionalarma

#Admin = dinosaurio pass= dino1234

#Esta son las APIs de los datos de el modelo Materia
class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = horas
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = datoshorario
        fields = ('user', 'semestre')
        depth = 1

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosmateria
        fields = ('materia', 'profesor', 'horario', 'grupo')
        depth = 1

#Esta es la API del modelo usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosusuario
        fields = '__all__'
