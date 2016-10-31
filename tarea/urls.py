from django.conf.urls import url
from .views import Agregar_tarea

urlpatterns = [
    url(r'^alertas', Agregar_tarea.as_view(), name='alerta'),
]
