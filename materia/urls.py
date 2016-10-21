from django.conf.urls import url
from .views import Materia, Detalles

urlpatterns = [
    url(r'^horario', Materia.as_view(), name='materia'),
    url(r'^detalle/(?P<pk>[0-9]+)/$', Detalles.as_view(), name='editar')
    # url(r'^materias/', Horario.as_view(), name='materias'),
]
