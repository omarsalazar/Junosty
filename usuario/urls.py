from django.conf.urls import url
from django.contrib import admin
from .views import Registro, Login, Index

urlpatterns = [
    url(r'^registro/', Registro.as_view(), name='registro'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^index/', Index.as_view(), name='index'),
]
