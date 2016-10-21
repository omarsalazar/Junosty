from django.conf.urls import url
from .views import Materia

urlpatterns = [
    url(r'^horario', Materia.as_view(), name='materia'),
    # url(r'^materias/', Horario.as_view(), name='materias'),
]
