from django.conf.urls import url
from .views import horario_list, hora_list, materia_list, usuario_list
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

    url(r'^api_usuario/$',
        csrf_exempt(usuario_list),
        name='api_usuario'
    ),
]
