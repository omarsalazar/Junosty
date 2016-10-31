from tares.models import tarea, alarmatarea, repeticiontarea

def set_tarea(datosTarea):
    try:
        tarea = tarea()
        tarea.id_tarea = datosTarea.get('tarea')
        tarea.descripcion = datosTarea.get('descripcion')
        tarea.materia = datosTarea.get('materia')
        tarea.materia = datosTarea.get('fecha_entrega')
        tarea.save()
    except Exception as e:
        print(e)
        print(type(e))
