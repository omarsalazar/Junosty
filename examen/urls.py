from django.conf.urls import url
from .views import Agregar_examen, Detalles

urlpatterns = [
    url(r'^alertas', Agregar_examen.as_view(), name='alerta'),
    url(r'^detalle/(?P<pk>[0-9]+)/$', Detalles.as_view(), name='editar')
]
