from django.contrib import admin
from datetime import datetime
from .models import datosusuario
from examen.models import examen, alarmaexamen, repeticionexamen
from tarea.models import tarea, alarmatarea, repeticiontarea
from semestre.models import semestre, vacaciones
from materia.models import datoshorario, datosmateria, horas


@admin.register(datosusuario)
class adminUsuario(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)


@admin.register(datoshorario)
class adminHorario(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)


@admin.register(datosmateria)
class adminMateria(admin.ModelAdmin):
    list_display = ('id', 'materia', 'profesor', 'horario')
    list_filter = ('id', 'materia', 'profesor', 'horario')


@admin.register(horas)
class adminHoras(admin.ModelAdmin):
    list_display = ('hora', 'fin', 'fecha', 'materia')
    list_filter = ('hora', 'fin', 'fecha', 'materia')
