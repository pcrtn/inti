# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0022_opcionesd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcionesd',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]