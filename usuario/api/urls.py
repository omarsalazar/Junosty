from django.conf.urls import url
from .views import horario_list, hora_list
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^horario/$',
        csrf_exempt(horario_list),
        name='horario'
    ),
    url(r'^horas/$',
        csrf_exempt(hora_list),
        name='horas'
    ),
]
