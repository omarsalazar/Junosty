from django.shortcuts import render
from django.views.generic import View

class Materia(View):
    def get(self, request):
        template_name = 'materias.html'
        return render(request, template_name)
