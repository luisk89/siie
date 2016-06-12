# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0003_alumnocalificacion_revalidacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='alta_date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
