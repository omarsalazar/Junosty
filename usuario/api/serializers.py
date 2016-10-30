from rest_framework import serializers
from materia.models import datoshorario, datosmateria, horas
from usuario.models import datosusuario
from semestre.models import semestre, vacaciones
from examen.models import examen, alarmaexamen, repeticionexamen
from tarea.models import tarea, alarmatarea, repeticiontarea

#Admin = dinosaurio pass= dino1234

#Estas son las APIs de los datos de el modelo "materia"
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

#Esta es la API del modelo "usuario"
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosusuario
        fields = '__all__'

#Estas son las APIs del modelo "semestre"
class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = semestre
        fields = '__all__'

class VacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vacaciones
        fields = '__all__'

#Estas son las APIs del modelo "examen"
class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = examen
        fields = '__all__'

class AlarmaExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = alarmaexamen
        fields = '__all__'

class RepeticionAlarmaExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = repeticionexamen
        fields = '__all__'

#Estas son las APIs del modelo "tarea"
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields = '__all__'

class AlarmaTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = alarmatarea
        fields = '__all__'

class RepeticionAlarmaTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = repeticiontarea
        fields = '__all__'
