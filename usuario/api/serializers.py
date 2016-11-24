from rest_framework import serializers
from materia.models import datoshorario, datosmateria, horas
from usuario.models import datosusuario
from semestre.models import semestre, vacaciones
from examen.models import examen, alarmaexamen, repeticionexamen
from tarea.models import tarea, alarmatarea, repeticiontarea


class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = horas
        fields = ('hora', 'fin', 'fecha', 'materia')


class MateriaSerializer(serializers.ModelSerializer):
    materias = HoraSerializer(many=True)

    class Meta:
        model = datosmateria
        fields = ('materia', 'profesor', 'horario', 'materias')


class HorarioSerializer(serializers.ModelSerializer):
    horarios = MateriaSerializer(many=True)

    class Meta:
        model = datoshorario
        fields = ('user', 'semestre', 'horarios')
        depth = 1
        paginate_by = None


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosusuario
        fields = '__all__'


class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = semestre
        fields = '__all__'


class VacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vacaciones
        fields = '__all__'


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
