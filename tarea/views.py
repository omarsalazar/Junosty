from django.shortcuts import render
from django.views.generic import View

class Tarea(View):
    def get(self, request):
        template_name = 'alertas.html'
        return render(request, template_name)
