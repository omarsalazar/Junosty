# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosusuario',
            name='curp',
        ),
        migrations.RemoveField(
            model_name='datosusuario',
            name='fecha_nacimiento',
        ),
    ]
