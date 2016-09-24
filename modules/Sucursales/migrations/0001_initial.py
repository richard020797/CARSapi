# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Marcas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('idMarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Marcas.Marca')),
            ],
        ),
    ]
