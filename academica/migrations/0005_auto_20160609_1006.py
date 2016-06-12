# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0004_auto_20160609_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='matricula',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
    ]
