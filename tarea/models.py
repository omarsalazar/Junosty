from django.db import models
from materia.models import datosmateria

#Aqui inicia la parte de las tareas
class tarea(models.Model):
    id_tarea = models.CharField(blank=False, null=False, max_length=100)
    descripcion = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(datosmateria, blank=False, null=False)
    fecha_entrega = models.DateTimeField(blank=False, null=False)

class alarmatarea(models.Model):
    id_alarmatarea = models.CharField(blank=True, null=True, max_length=100)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    id_tarea = models.ForeignKey(tarea, blank=False, null=False)

class repeticionalarma(models.Model):
    horaalarma = models.DateTimeField(blank=True, null=True)
    id_alarmatarea = models.ForeignKey(alarmatarea, blank=False, null=False)
#Aquí finaliza la parte de las tareas