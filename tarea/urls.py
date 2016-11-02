from django.conf.urls import url
from .views import Agregar_tarea, Detalles

urlpatterns = [
    url(r'^alertas', Agregar_tarea.as_view(), name='alerta'),
    url(r'^detalle/(?P<pk>[0-9]+)/$', Detalles.as_view(), name='editar')
]
