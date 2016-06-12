# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0006_auto_20160609_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='materia',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='materia_id',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
