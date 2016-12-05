# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0012_modelo_tipo_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=50)),
                ('observacion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Modelo')),
            ],
        ),
    ]
