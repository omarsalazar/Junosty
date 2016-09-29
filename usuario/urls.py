from django.conf.urls import url
from django.contrib import admin
from .views import Registro, Login, Index, Logout, ModificarDatos

urlpatterns = [
    url(r'^registro/', Registro.as_view(), name='registro'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^modificardatos/', ModificarDatos.as_view(), name='modificar'),
]
