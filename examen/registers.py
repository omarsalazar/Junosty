from examen.models import examen, alarmaexamen, repeticionexamen
from materia.models import datosmateria
from django.contrib.auth.models import User


def set_examen(datosExamen):
    try:
        examen1 = examen()
        examen1.id_examen = datosExamen.get('examen')
        examen1.descripcion = datosExamen.get('descripcion')
        obj_materia = datosmateria.objects.get(
            materia=datosExamen.get('materia')
            )
        examen1.materia = obj_materia
        examen1.fecha_entrega = datosExamen.get('fecha_entrega')
        examen1.user = User.objects.get(username=datosExamen.get('user'))
        examen1.save()
    except Exception as e:
        print('no guardo')
        print(e)
        print(type(e))


def cambiar_examen(datosExamen):
    try:
        examencito = examen.objects.get(id=(datosExamen.get('id')))
        examencito.id_examen = datosExamen.get('examen')
        examencito.descripcion = datosExamen.get('descripcion')
        print(datosExamen.get('materia'))
        obj_materia = datosmateria.objects.get(
            materia=datosExamen.get('materia')
            )
        examencito.materia = obj_materia
        if datosExamen.get('fecha_entrega') == '' or None:
            pass
        else:
            examencito.fecha_entrega = datosExamen.get('fecha_entrega')
        examencito.save()
    except Exception as e:
        print(e)
        print(type(e))


def eliminar_examenes(request):
    print('llego')
    eliminado = request.POST.get('id')
    try:
        obj_eliminado = examen.objects.all().filter(id=eliminado)
        obj_eliminado.delete()
    except Exception as e:
        print('error')
        print(e)
        print(type(e))
