from django.shortcuts import render, redirect
from django.views.generic import View
from tarea.models import tarea
from .registers import *
from materia.models import datosmateria


class Agregar_tarea(View):
    def get(self, request):
        template_name = 'alertas.html'
        try:
            tareas = tarea.objects.all().filter(user=request.user)
            materias = datosmateria.objects.all()
            context = {
                'tarea': tareas,
                'materias': materias
            }
        except:
            context = {}
        return render(request, template_name, context)

    def post(self, request):
        action = request.POST.get('action')
        print(action)
        if action == 'agregar':
            try:
                set_tarea(request.POST)
                return redirect('/tarea/alertas')
            except Exception as e:
                print('he fallado')
                print(e)
                print(type(e))
                return redirect('/tarea/alertas')

        elif action == 'eliminar':
            try:
                eliminar_tareas(request)
                return redirect('/tarea/alertas')
            except Exception as e:
                print(e)
                print(type(e))
                return redirect('/tarea/alertas')


class Detalles(View):
    def get(self, request, pk):
        tareita = tarea.objects.get(pk=pk)
        template_name = 'tarea_detail.html'
        materias = datosmateria.objects.all()
        context = {
            'tarea': tareita,
            'materias': materias
        }
        return render(request, template_name, context)

    def post(self, request, pk):
        try:
            cambiar_tarea(request.POST)
            return redirect('/tarea/alertas')
        except Exception as e:
            print(e)
            print(type(e))
            return redirect('/tarea/alertas')
