from django.conf.urls import url
from .views import horario_list, hora_list, materia_list, usuario_list, semestre_list, vacaciones_list, examen_list, alarmaexamen_list, repeticionalarmaexamen_list, tarea_list, alarmatarea_list, repeticionalarmatarea_list
from django.views.decorators.csrf import csrf_exempt

#Urls de las APIs
urlpatterns = [
    url(r'^horario/$',
        csrf_exempt(horario_list),
        name='horario'
    ),
    url(r'^horas/$',
        csrf_exempt(hora_list),
        name='horas'
    ),
    url(r'^materia/$',
        csrf_exempt(materia_list),
        name='materia'
    ),

    url(r'^usuario/$',
        csrf_exempt(usuario_list),
        name='usuario'
    ),

    url(r'^semestre/$',
        csrf_exempt(semestre_list),
        name='semestre'
    ),

    url(r'^vacaciones/$',
        csrf_exempt(vacaciones_list),
        name='vacaciones'
    ),

    url(r'^examen/$',
        csrf_exempt(examen_list),
        name='examen'
    ),

    url(r'^alarmaexamen/$',
        csrf_exempt(alarmaexamen_list),
        name='alarmaexamen'
    ),

    url(r'^repeticionalarmaexamen/$',
        csrf_exempt(repeticionalarmaexamen_list),
        name='repeticionalarmaexamen'
    ),

    url(r'^tarea/$',
        csrf_exempt(tarea_list),
        name='tarea'
    ),

    url(r'^alarmatarea/$',
        csrf_exempt(alarmatarea_list),
        name='alarmatarea'
    ),

    url(r'^repeticionalarmatarea/$',
        csrf_exempt(repeticionalarmatarea_list),
        name='repeticionalarmatarea'
    ),


]
