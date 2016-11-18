# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ISBN', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=20)),
                ('imagen', models.FileField(blank=True, upload_to='', null=True)),
                ('autor', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dpi', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=30)),
                ('prestamo', models.ForeignKey(to='blogbiblioteca.Libro')),
            ],
            options={
                'ordering': ('dpi',),
            },
        ),
    ]
