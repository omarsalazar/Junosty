from django.db import models
from django.contrib.auth.models import User
from materia.models import datosmateria


#Aquí inicia la parte de los examenes
class examen(models.Model):
    id_examen = models.CharField(blank=False, null=False, max_length=100)
    id_tarea = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
    fecha_entrega = models.DateTimeField(blank=False, null=False)


class alarmaexamen(models.Model):
    id_alarmaexamen = models.CharField(blank=False, null=False, max_length=100)
    fecha_entrega = models.DateTimeField(blank=False, null=False)
    id_examen = models.ForeignKey(examen, blank=False, null=False)

class repeticionexamen(models.Model):
    horaexamen = models.DateTimeField(blank=False, null=False)
    id_alarmaexamen = models.ForeignKey(alarmaexamen, blank=False, null=False)
#Aquí finaliza la parte de los examenes
