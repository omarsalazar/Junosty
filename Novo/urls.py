from django.conf.urls import url, include
from django.contrib import admin
from usuario import urls as urlsUsuario
from usuario.api import urls as materiasAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', include(urlsUsuario, namespace='usuario')),
    url(r'^horario/', include(materiasAPI, namespace='horario'))
]
