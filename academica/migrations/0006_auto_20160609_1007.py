# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0005_auto_20160609_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificaciones',
            old_name='matricula',
            new_name='matricula_id',
        ),
    ]
