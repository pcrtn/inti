# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseno', '0003_auto_20170404_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleproducto',
            name='idProducto',
        ),
        migrations.AddField(
            model_name='producto',
            name='presupuesto',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='total',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidades',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='detalleProducto',
        ),
    ]
