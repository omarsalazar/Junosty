from rest_framework import serializers
from materia.models import datoshorario, datosmateria, horas
from usuario.models import datosusuario

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = horas
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    horas = HoraSerializer(many=True)
    class Meta:
        model = datosmateria
        fields = ('id','materia','profesor','horario','horas')

class HorarioSerializer(serializers.ModelSerializer):
    materias = MateriaSerializer(many=True)
    class Meta:
        model = datoshorario
        fields = ('user', 'materias')
        depth = 1
