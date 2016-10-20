from django.contrib import admin
from .models import datosusuario, datoshorario, datosmateria, horas

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
    list_display = ('materia','profesor','horario')
    list_filter = ('materia','profesor','horario')

@admin.register(horas)

class adminHoras(admin.ModelAdmin):
    list_display = ('hora', 'fecha', 'materia')
    list_filter = ('hora', 'fecha', 'materia')
