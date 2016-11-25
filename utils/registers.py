from usuario.models import datosusuario
from django.contrib.auth.models import User
from usuario.models import datosusuario
from django.core.exceptions import ObjectDoesNotExist
from materia.models import horas


def registro(datosRegistro):
    try:
        usuario = datosusuario()
        usuario.user = User.objects.get(username=datosRegistro.get('correo'))
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
        User.objects.create_user(username=username, password=password)
    except Exception as e:
        print(e)
        print(type(e))


def modificaUsuario(datosRegistro):
    print('llego')
    try:
        user = User.objects.get(username=datosRegistro.user.username)
        usuario = datosusuario.objects.get(user=user)
        if datosRegistro.POST.get('usuario') is None or '':
            pass
        else:
            usuario.nombre = datosRegistro.POST.get('usuario')
        if datosRegistro.POST.get('apellidos') is None or '':
            pass
        else:
            usuario.apellidos = datosRegistro.POST.get('apellidos')
        if datosRegistro.POST.get('contrasena') is None or '':
            user.set_password(datosRegistro.POST.get('contrasena'))
            usuario.contrasena = datosRegistro.POST.get('contrasena')
        usuario.save()
        user.save()
    except User.DoesNotExist as e:
        print(e)
        print(type(e))
    except datosusuario.DoesNotExist as e:
        print(e)
        print(type(e))
    except Exception as e:
        print(e)
        print(type(e))


def cambiar_hora(request):
    print('llego a cambiar hora')
    try:
        hora = horas.objects.get(id=request.POST.get('aidi'))
        hora.fin = request.POST.get('fin')
        hora.hora = request.POST.get('hora')
        hora.fecha = request.POST.get('dia')
        hora.save()
    except horas.DoesNotExist as e:
        print(e)
        print(type(e))
    except Exception as e:
        print(e)
        print(type(e))


def eliminar_hora(request):
    try:
        hora = horas.objects.all().filter(id=request.POST.get('aidi'))
        hora.delete()
    except horas.DoesNotExist:
        print(e)
        print(type(e))
    except Exception as e:
        print(e)
        print(type(e))
