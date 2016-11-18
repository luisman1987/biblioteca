# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogbiblioteca', '0003_auto_20161118_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='imagen',
        ),
    ]
