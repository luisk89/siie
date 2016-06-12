# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0008_auto_20160609_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='materia_id',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='matricula_id',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='plan_id',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='semestre_id',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='materia',
            field=models.ForeignKey(to='academica.Materias', to_field='clave', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='matricula',
            field=models.ForeignKey(to='academica.Alumnos', to_field='matricula', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='plan',
            field=models.ForeignKey(to='academica.PlanEstudio', to_field='clave_plan', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='semestre',
            field=models.ForeignKey(to='academica.CicloSemestral', to_field='clave', null=True),
            preserve_default=True,
        ),
    ]
