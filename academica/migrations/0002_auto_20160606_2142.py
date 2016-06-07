# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupos',
            name='horarios',
        ),
        migrations.AddField(
            model_name='grupos',
            name='horario',
            field=models.ForeignKey(null=True, blank=True, to='academica.Horario'),
            preserve_default=True,
        ),
    ]
