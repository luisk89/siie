# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0002_remove_alumnocalificacion_revalidacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnocalificacion',
            name='revalidacion',
            field=models.SmallIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
