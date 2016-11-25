# from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import qrcode
from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile


class datosusuario(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    apellidos = models.CharField(blank=False, null=False, max_length=100)
    no_boleta = models.CharField(blank=False, null=False, max_length=10)
    contrasena = models.CharField(blank=False, null=False, max_length=100)
    correo = models.EmailField(blank=True, null=True, max_length=100)
    qr = models.CharField(null=True, blank=True, max_length=50)

    def save(self, *args, **kwargs):
        try:
            img = qrcode.make(self.no_boleta)
            self.qr = str(self.generate_qrcode())
        except Exception as e:
            print(e)
            print(type(e))
        super(datosusuario, self).save(*args, **kwargs)

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(self.no_boleta + ' - ' + self.nombre + self.apellidos)
        qr.make(fit=True)

        filename = '{}_qrcode.png'.format(self.nombre)

        img = qr.make_image()
        img.save('media/' + filename)
        return 'media/' + filename

    def __str__(self):
        return "{}".format(self.nombre)
