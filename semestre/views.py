from django.shortcuts import render
from django.views.generic import View
from materia.models import datosmateria, horas, datoshorario


class Horario(View):
    def get(self, request):
        template_name = 'horario.html'
        horario = datoshorario.objects.filter(user=request.user)
        materias = datosmateria.objects.filter(horario=horario)
        mate = datosmateria.objects.values_list(
            'id',
            flat=True).filter(
                horario=horario
            )
        dic = list(mate)
        hora = horas.objects.filter(materia__in=dic)
        context = {
            'materita': materias,
            'horitas': hora
        }
        return render(request, template_name, context)
