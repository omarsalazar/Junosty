# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class datosusuario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    apellidos = models.CharField(blank=False, null=False, max_length=100)
    curp = models.CharField(blank=False, null=False, max_length=18)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    no_boleta = models.CharField(blank=False, null=False, max_length=10)
    carrera = models.CharField(blank=False, null=False, max_length=50)
    contrasena = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return "{}".format(self.nombre)
