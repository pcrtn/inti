# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0025_auto_20170330_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgpyc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='imagenesProyecto/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto')),
            ],
        ),
    ]