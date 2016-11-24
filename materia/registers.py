from .models import *
from semestre.models import *
import uuid


def guardar_materia(request):
    horario = datoshorario()
    materia = datosmateria()
    hora = horas()
    seme = semestre()
    valor = 0
    try:
        obj_horario = datoshorario.objects.get(user=request.user)
    except:
        aidi_seme = str(uuid.uuid4().fields[-1])[:5]+str(request.user.username)
        try:
            seme.id_semestre = aidi_seme
            seme.user = request.user
            seme.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            horario.user = request.user
            horario.semestre = semestre.objects.get(id_semestre=aidi_seme)
            horario.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            materia.materia = request.POST.get('materia')
            materia.profesor = request.POST.get('profesor')
            materia.grupo = request.POST.get('grupo')
            materia.horario = datoshorario.objects.get(user=request.user)
            materia.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            hora.materia = materia.objects.get(
                materia=request.POST.get('materia')
                )
            hora.save()
        except Exception as e:
            print(e)
            print(type(e))
        valor = 2
    print(valor)
    if obj_horario is not None:
        try:
            materia.materia = request.POST.get('materia')
            materia.profesor = request.POST.get('profesor')
            materia.grupo = request.POST.get('grupo')
            materia.horario = datoshorario.objects.get(user=request.user)
            materia.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            hora.materia = materia.objects.get(
                materia=request.POST.get('materia')
                )
            hora.save()
        except Exception as e:
            print(e)
            print(type(e))
    else:
        aidi_seme = str(uuid.uuid4().fields[-1])[:5]+str(request.user.username)
        try:
            seme.id_semestre = aidi_seme
            seme.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            horario.user = request.user
            horario.semestre = seme.objects.get(id_semestre=aidi_seme)
        except Exception as e:
            print(e)
            print(type(e))
        try:
            materia.materia = request.POST.get('materia')
            materia.profesor = request.POST.get('profesor')
            materia.grupo = request.POST.get('grupo')
            materia.horario = datoshorario.objects.get(user=request.user)
            materia.save()
        except Exception as e:
            print(e)
            print(type(e))
        try:
            hora.materia = materia.objects.get(
                materia=request.POST.get('materia')
                )
            hora.save()
        except Exception as e:
            print(e)
            print(type(e))


def eliminar_materias(request):
    materia = request.POST.get('id')
    try:
        obj_materia = datosmateria.objects.all().filter(id=materia)
        obj_materia.delete()
    except Exception as e:
        print('error')
        print(e)
        print(type(e))


def cambiar_materia(request):
    materia = request.POST.get('id')
    try:
        obj_materia = datosmateria.objects.get(id=materia)
        obj_materia.materia = request.POST.get('materia')
        obj_materia.profesor = request.POST.get('profesor')
        obj_materia.grupo = request.POST.get('grupo')
        obj_materia.save()
    except Exception as e:
        print(e)
        print(type(e))
    try:
        hrs = horas()
        print(request.POST.get('dia'))
        hrs.fecha = request.POST.get('dia')
        hrs.hora = request.POST.get('hora')
        hrs.fin = request.POST.get('fin')
        hrs.materia = datosmateria.objects.get(id=materia)
        hrs.save()
    except Exception as e:
        print(e)
        print(type(e))
