from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.
class HorasTestCase(TestCase):
    def setUp(self):
        hoy = datetime.now()
        usuario = User.objects.create_user(username = "Omar", password = "password")
        semestret = semestre.objects.create(id_semestre = "1451", fecha_inicio = hoy,
        fecha_final = hoy, user = usuario)
        horario = datoshorario.objects.create(user = usuario, semestre = semestret)
        materia = datosmateria.objects.create(materia = "Orientacion", profesor = "Hilda Moreno",
        grupo = "1234", horario = horario)

    def test(self):
        materia = datosmateria.objects.get(materia = "Orientacion")
        return self.assertEqual(materia.materia, 'Matematicas')
