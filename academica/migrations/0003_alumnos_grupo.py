# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0002_grupos_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='grupo',
            field=models.ForeignKey(to_field='clave', to='academica.Grupos', null=True, blank=True),
            preserve_default=True,
        ),
    ]
