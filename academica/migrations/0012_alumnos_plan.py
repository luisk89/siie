# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0011_remove_alumnos_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='plan',
            field=models.ForeignKey(null=True, to_field='clave_plan', to='academica.PlanEstudio'),
            preserve_default=True,
        ),
    ]
