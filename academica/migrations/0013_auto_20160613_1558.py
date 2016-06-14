# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0012_alumnos_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='plan',
            field=models.ForeignKey(to='academica.PlanEstudio', null=True, blank=True, to_field='clave_plan'),
            preserve_default=True,
        ),
    ]
