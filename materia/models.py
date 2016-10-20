from django.db import models
from django.contrib.auth.models import User
from semestre.models import semestre


class datoshorario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    semestre = models.ForeignKey(semestre, blank=False, null=False)

class datosmateria(models.Model):
    materia = models.CharField(blank=False, null=False, max_length=50)
    profesor = models.CharField(blank=False, null=False, max_length=60)
    horario = models.ForeignKey(datoshorario, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.materia)

class horas(models.Model):
    hora = models.DateTimeField(blank=False, null=False)
    fecha = models.DateTimeField(blank=False, null=False)
    materia =models.ForeignKey(datosmateria, blank=False, null=False)
