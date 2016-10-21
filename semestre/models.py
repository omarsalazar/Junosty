from django.db import models
from django.contrib.auth.models import User

class semestre(models.Model):
    id_semestre = models.CharField(blank=True, max_length=20)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

class vacaciones(models.Model):
    id_vacaciones = models.CharField(blank=True, max_length=20)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_final = models.DateField(blank=False, null=False)
