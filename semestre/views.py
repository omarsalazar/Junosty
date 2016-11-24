from django.shortcuts import render
from django.views.generic import View


class Horario(View):
    def get(self, request):
        template_name = 'horario.html'
        return render(request, template_name)
