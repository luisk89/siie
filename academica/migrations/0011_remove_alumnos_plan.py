# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0010_remove_alumnos_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='plan',
        ),
    ]
