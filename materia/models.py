from django.db import models
from django.contrib.auth.models import User
from semestre.models import semestre


class datoshorario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    semestre = models.ForeignKey(
        semestre, blank=False, null=False, related_name='semestres'
        )


class datosmateria(models.Model):
    materia = models.CharField(blank=False, null=False, max_length=50)
    profesor = models.CharField(blank=False, null=False, max_length=60)
    horario = models.ForeignKey(
        datoshorario, blank=False, null=False, related_name='horarios'
        )
    grupo = models.CharField(blank=True, null=True, max_length=6)

    def __str__(self):
        return '{}'.format(self.materia)


class horas(models.Model):
    hora = models.CharField(blank=True, null=True, max_length=30)
    fin = models.CharField(blank=True, null=True, max_length=30)
    fecha = models.CharField(blank=True, null=True, max_length=30)
    materia = models.ForeignKey(
        datosmateria, blank=False, null=False, related_name='materias'
        )


class semana(models.Model):
    dia = models.CharField(blank=False, null=False, max_length=10)
    horai = models.CharField(blank=True, null=False, max_length=6)
    horaf = models.CharField(blank=True, null=False, max_length=6)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
