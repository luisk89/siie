# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0013_auto_20160613_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='semestre',
            field=models.ForeignKey(to_field='clave', to='academica.CicloSemestral'),
            preserve_default=True,
        ),
    ]
