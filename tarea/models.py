from django.db import models
from django.contrib.auth.models import User
from materia.models import datosmateria
from datetime import datetime

#Aqui inicia la parte de las tareas
class tarea(models.Model):
    id_tarea = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
    fecha_entrega = models.DateTimeField(blank=False, null=False)

class alarmatarea(models.Model):
    id_alarmatarea = models.CharField(blank=False, null=False, max_length=100)
    fecha_entrega = models.DateTimeField(blank=False, null=False)
    id_tarea = models.ForeignKey(tarea, blank=False, null=False)

class repeticionalarma(models.Model):
    horaalarma = models.DateTimeField(blank=False, null=False)
    id_alarmatarea = models.ForeignKey(alarmatarea, blank=False, null=False)
#Aquí finaliza la parte de las tareas
