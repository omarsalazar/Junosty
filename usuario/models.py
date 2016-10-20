# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class datosusuario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    apellidos = models.CharField(blank=False, null=False, max_length=100)
    no_boleta = models.CharField(blank=False, null=False, max_length=10)
    carrera = models.CharField(blank=False, null=False, max_length=50)
    contrasena = models.CharField(blank=False, null=False, max_length=100)

class datoshorario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)

class datosmateria(models.Model):
    materia = models.CharField(blank=False, null=False, max_length=50)
    profesor = models.CharField(blank=False, null=False, max_length=60)
    horario = models.ForeignKey(datoshorario, blank=False, null=False, related_name='materias')

    def __str__(self):
        return '{}'.format(self.materia)

class horas(models.Model):
    hora = models.DateTimeField(blank=False, null=False)
    fecha = models.DateTimeField(blank=False, null=False)
    materia =models.ForeignKey(datosmateria, blank=False, null=False, related_name='horas')
