# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0003_alumnos_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='semestre',
            field=models.ForeignKey(to='academica.CicloSemestral', to_field='clave'),
            preserve_default=True,
        ),
    ]
