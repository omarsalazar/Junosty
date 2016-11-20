#El proposito de este archivo es hacer funciones que se van a necesitar en todo el proyecto
from usuario.models import datosusuario
from django.contrib.auth.models import User
#Esta función va a registrar al usuario.
def registro(datosRegistro):
    try:
        usuario = datosusuario()
        usuario.user = User.objects.get(username=datosRegistro.get('no_boleta'))
        usuario.nombre = datosRegistro.get('nombre')
        usuario.apellidos = datosRegistro.get('apellidos')
        usuario.no_boleta = datosRegistro.get('no_boleta')
        usuario.carrera = datosRegistro.get('carrera')
        usuario.contrasena = datosRegistro.get('contrasena')
        usuario.correo = datosRegistro.get('correo')
        usuario.save()
    except Exception as e:
        print(e)
        print(type(e))

def registroUser(username, password):
    try:
        User.objects.create_user(username=username,password=password)
    except Exception as e:
        print(e)
        print(type(e))

def modificaUsuario(datosRegistro):
    try:
        user = User.objects.get(username=datosRegistro.user.username)
        usuario = datosusuario.objects.get(user=user)
        usuario.nombre = datosRegistro.POST.get('nombre')
        usuario.apellidos = datosRegistro.POST.get('apellidos')
        usuario.contrasena = datosRegistro.POST.get('contrasena')
        user.set_password(datosRegistro.POST.get('contrasena'))
        usuario.save()
        user.save()
    except Exception as e:
        print(e)
        print(type(e))
