from django.contrib import admin
from .models import datosusuario

@admin.register(datosusuario)

class adminUsuario(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
