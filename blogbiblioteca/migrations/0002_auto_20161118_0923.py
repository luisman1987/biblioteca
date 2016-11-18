# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogbiblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fechaprestamo', models.DateField()),
                ('fechadevolucionp', models.DateField()),
                ('fechadevolucionr', models.DateField()),
                ('libro', models.ManyToManyField(to='blogbiblioteca.Libro')),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='prestamo',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='persona',
            field=models.ForeignKey(to='blogbiblioteca.Persona'),
        ),
    ]
