from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import MateriaForm
from .registers import guardar_materia
from .models import *

class Materia(View):
    def get(self, request):
        template_name = 'materias.html'
        materia = MateriaForm()
        try:
            horario = datoshorario.objects.get(user=request.user)
            materias = datosmateria.objects.all().filter(horario=horario)
        except:
            materias = {}
        context = {
            'form': materia,
            'materias': materias
        }
        return render(request, template_name, context)

    def post(self, request):
        form = MateriaForm(request.POST)
        if form.is_valid():
            try:
                guardar_materia(request)
                return redirect('/materia/horario')
            except Exception as e:
                print('he fallado')
                print(e)
                print(type(e))
                return redirect('/materia/horario')
