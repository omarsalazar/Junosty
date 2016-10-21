from django.conf.urls import url
from .views import Tarea

urlpatterns = [
    url(r'^alertas', Tarea.as_view(), name='alerta'),
]
