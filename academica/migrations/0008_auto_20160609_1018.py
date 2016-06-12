# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0007_auto_20160609_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='semestre',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='plan_id',
            field=models.CharField(max_length=50, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='semestre_id',
            field=models.CharField(max_length=50, blank=True, null=True),
            preserve_default=True,
        ),
    ]
