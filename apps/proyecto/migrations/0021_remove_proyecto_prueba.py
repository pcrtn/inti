# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0020_auto_20170330_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='prueba',
        ),
    ]
