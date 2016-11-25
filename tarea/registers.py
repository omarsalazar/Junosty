from tarea.models import tarea, alarmatarea, repeticiontarea
from materia.models import datosmateria
from django.contrib.auth.models import User


def set_tarea(datosTarea):
    try:
        tarea1 = tarea()
        tarea1.id_tarea = datosTarea.get('tarea')
        tarea1.descripcion = datosTarea.get('descripcion')
        obj_materia = datosmateria.objects.get(
            materia=datosTarea.get('materia')
            )
        tarea1.materia = obj_materia
        tarea1.fecha_entrega = datosTarea.get('fecha_entrega')
        tarea1.user = User.objects.get(username=datosTarea.get('user'))
        tarea1.save()
    except Exception as e:
        print('no guardo')
        print(e)
        print(type(e))


def cambiar_tarea(datosTarea):
    try:
        tareita = tarea.objects.get(id=(datosTarea.get('id')))
        tareita.id_tarea = datosTarea.get('tarea')
        tareita.descripcion = datosTarea.get('descripcion')
        obj_materia = datosmateria.objects.get(
            materia=datosTarea.get('materia')
            )
        tareita.materia = obj_materia
        if datosTarea.get('fecha_entrega') == '' or None:
            pass
        else:
            tareita.fecha_entrega = datosTarea.get('fecha_entrega')
        tareita.save()
    except Exception as e:
        print(e)
        print(type(e))


def eliminar_tareas(request):
    print('llego')
    eliminado = request.POST.get('id')
    try:
        obj_eliminado = tarea.objects.all().filter(id=eliminado)
        obj_eliminado.delete()
    except Exception as e:
        print('error')
        print(e)
        print(type(e))
