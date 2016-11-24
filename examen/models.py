from django.db import models
from django.contrib.auth.models import User
from materia.models import datosmateria


class examen(models.Model):
    id_examen = models.CharField(blank=False, null=False, max_length=20)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
    fecha_entrega = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, blank=True, null=True)


class alarmaexamen(models.Model):
    id_alarmaexamen = models.CharField(blank=True, null=True, max_length=100)
    fecha_entrega = models.DateField(blank=True, null=True)
    id_examen = models.ForeignKey(examen, blank=False, null=False)


class repeticionexamen(models.Model):
    horaexamen = models.TimeField(blank=True, null=True)
    id_alarmaexamen = models.ForeignKey(alarmaexamen, blank=False, null=False)
