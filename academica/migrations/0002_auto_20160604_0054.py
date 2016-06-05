# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='condicionado',
            field=models.SmallIntegerField(blank=True, verbose_name='Status', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='firma',
            field=models.ImageField(blank=True, upload_to='firma'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='lugar_nac',
            field=models.CharField(blank=True, verbose_name='Lugar de nacimiento', max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='no_expediente',
            field=models.CharField(unique=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciohoras',
            name='alumno',
            field=models.ForeignKey(unique=True, to='academica.Alumnos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciohoras',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='liberar'),
            preserve_default=True,
        ),
    ]
