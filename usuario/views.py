from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import registroForm, inicioForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

class Registro(View):
    def get(self, request):
        template_name = 'usuario/registro.html'
        form = registroForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        datos = registroForm(request.POST)
        username = request.POST.get('no_boleta')
        password = request.POST.get('contrasena')
        if datos.is_valid():
            datos.save()
            User.objects.create_user(username=username,password=password)
            return redirect('usuario:login')

        else:
            return redirect('usuario:registro')

#Aquí se crea un método get y post para mandar y recibir los datos del login uwu
class Login(View):
    def get(self, request):
        template_name = 'usuario/login.html'
        form = inicioForm()
        context = {
            'loginform': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        username = request.POST.get('no_boleta')
        password = request.POST.get('contrasena')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('usuario:index')
        else:
            return redirect('usuario:login')

class Index(View):
    def get(self, request):
        template_name = 'usuario/index.html'
        return render(request, template_name)
