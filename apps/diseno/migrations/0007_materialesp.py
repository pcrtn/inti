# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseno', '0006_auto_20170410_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='materialesP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
