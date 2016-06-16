# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0015_auto_20160614_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='cal_final',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='calif1',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='calif1_res',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='calif2',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='calif2_res',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='status1_res',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='status2_res',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='cuarta',
            field=models.DecimalField(verbose_name='4ta Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='final',
            field=models.DecimalField(verbose_name='Calificacion Final', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='primera',
            field=models.DecimalField(verbose_name='1ra Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='quinta',
            field=models.DecimalField(verbose_name='5ta Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='segunda',
            field=models.DecimalField(verbose_name='2da Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='sexta',
            field=models.DecimalField(verbose_name='6ta Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='status4',
            field=models.IntegerField(verbose_name='Status', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='status5',
            field=models.IntegerField(verbose_name='Status', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='status6',
            field=models.IntegerField(verbose_name='Status', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='status_final',
            field=models.IntegerField(verbose_name='Status', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='tercera',
            field=models.DecimalField(verbose_name='3ra Calificacion', null=True, decimal_places=0, max_digits=3, blank=True),
            preserve_default=True,
        ),
    ]
