# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0012_auto_20170327_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tipoProyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.tipoProyecto'),
        ),
    ]
