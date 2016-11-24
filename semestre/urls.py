from django.conf.urls import url
from .views import Horario

urlpatterns = [
    url(r'^horario/', Horario.as_view(), name='calendario'),
]
