# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0014_auto_20160613_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='curp',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
