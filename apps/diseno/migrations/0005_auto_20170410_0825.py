# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseno', '0004_auto_20170405_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='presupuesto',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='total',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidades',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
