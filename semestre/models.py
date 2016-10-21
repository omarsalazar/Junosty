from django.db import models


class semestre(models.Model):
    id_semestre = models.CharField(blank=True, max_length=20)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_final = models.DateField(blank=False, null=False)

class vacaciones(models.Model):
    id_vacaciones = models.CharField(blank=True, max_length=20)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_final = models.DateField(blank=False, null=False)
