# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0016_remove_cliente_prueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fechaApr',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fechaEntDis',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fechaEntPro',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fechaMueFis',
            field=models.DateField(blank=True, null=True),
        ),
    ]
