# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0023_auto_20170330_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='selec',
            field=models.ManyToManyField(blank=True, null=True, to='proyecto.opcionesD'),
        ),
    ]
