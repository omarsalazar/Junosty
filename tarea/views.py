from django.shortcuts import render
from django.views.generic import View
from tarea.models import tarea

class Agregar_tarea(View):
     def get(self, request):
         template_name = 'alertas.html'
         try:
             tareas = tarea.objects.all().filter(user=request.user)
             context = {
                'tarea': tareas
             }
         except:
             context = {}

         return render(request, template_name, context)
