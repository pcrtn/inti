# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseno', '0008_producto_materiales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='materiales',
            field=models.ManyToManyField(blank=True, to='diseno.materialesP'),
        ),
    ]