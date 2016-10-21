from django.conf.urls import url, include
from django.contrib import admin
from usuario import urls as urlsUsuario
#from examen import urls as urlsExamen
from materia import urls as urlsMateria
from semestre import urls as urlsSemestre
from tarea import urls as urlsTarea
from usuario.api import urls as materiasAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', include(urlsUsuario, namespace='usuario')),
    # #url(r'^examen/', include(urlsExamen, namespace='examen')),
    # url(r'^materia', include(urlsMateria, namespace='materia')),
    # url(r'^tarea', include(urlsTarea, namespace='tarea')),
    # url(r'^semestre', include(urlsSemestre, namespace='semestre')),
    # url(r'^horario/', include(materiasAPI, namespace='horario'))
]
