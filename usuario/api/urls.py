from django.conf.urls import url
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    url(r'^horario/$',
        csrf_exempt(horario_list)
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
