from django.conf.urls import url, include
from django.contrib import admin
from usuario import urls as urlsUsuario
from usuario.views import Index
from materia import urls as urlsMateria
from semestre import urls as urlsSemestre
from tarea import urls as urlsTarea
from examen import urls as urlsExamen
from usuario.api import urls as materiasAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^usuario/', include(urlsUsuario, namespace='usuario')),
    url(r'^materia/', include(urlsMateria, namespace='materia')),
    url(r'^tarea/', include(urlsTarea, namespace='tarea')),
    url(r'^examen/', include(urlsExamen, namespace='examen')),
    url(r'^semestre/', include(urlsSemestre, namespace='semestre')),
    url(r'^apiv1/', include(materiasAPI, namespace='apiv1')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
