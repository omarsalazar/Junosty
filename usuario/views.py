from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import registroForm, inicioForm, modificarForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from utils.registers import registro, modificaUsuario, registroUser
# Create your views here.


class Perfil(View):
    def get(self, request):
        template_name = 'perfil.html'
        return render(request, template_name)


class Registro(View):
    def get(self, request):
        template_name = 'registro.html'
        form = registroForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        username = request.POST.get('correo')
        password = request.POST.get('contrasena')
        print(username)
        print(password)
        try:
            registroUser(username, password)
            registro(request.POST)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('usuario:perfil')

        except Exception as e:
            print(e)
            print(type(e))
            return redirect('usuario:registro')


class Login(View):
    def get(self, request):
        template_name = 'login.html'
        form = inicioForm()
        context = {
            'loginform': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        username = request.POST.get('no_boleta')
        password = request.POST.get('contrasena')

        # Esto sirve para auntentificar que lo que se guardo exista, si
        # existe entonces va a hacer el login, de lo contrario redirijira
        # al login
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('usuario:perfil')
        else:
            return redirect('usuario:login')


class Index(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)

def Logout(request):
    logout(request)
    return redirect('usuario:login')


class ModificarDatos(View):
    def get(self, request):
        template_name = 'usuario/modificar.html'
        form = modificarForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        try:
            modificaUsuario(request)
            return redirect('usuario:login')
        except Exception as e:
            print(e)
            print(type(e))
            return redirect('usuario:modficar')
