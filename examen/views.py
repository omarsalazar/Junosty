from django.shortcuts import render, redirect
from django.views.generic import View
from examen.models import examen
from .registers import *
from materia.models import datosmateria


class Agregar_examen(View):
    def get(self, request):
        template_name = 'alertas_examen.html'
        try:
            examenes = examen.objects.all().filter(user=request.user)
            materias = datosmateria.objects.all()
            context = {
                'examen': examenes,
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
                set_examen(request.POST)
                return redirect('/examen/alertas')
            except Exception as e:
                print('he fallado')
                print(e)
                print(type(e))
                return redirect('/examen/alertas')

        elif action == 'eliminar':
            try:
                eliminar_examenes(request)
                return redirect('/examen/alertas')
            except Exception as e:
                print(e)
                print(type(e))
                return redirect('/examen/alertas')


class Detalles(View):
    def get(self, request, pk):
        examencito = examen.objects.get(pk=pk)
        template_name = 'examen_detail.html'
        materias = datosmateria.objects.all()
        context = {
            'examen': examencito,
            'materias': materias
        }
        return render(request, template_name, context)

    def post(self, request, pk):
        try:
            cambiar_examen(request.POST)
            return redirect('/examen/alertas')
        except Exception as e:
            print(e)
            print(type(e))
            return redirect('/examen/alertas')


# Create your views here.
