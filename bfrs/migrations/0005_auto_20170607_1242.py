# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-07 04:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0004_auto_20170529_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bushfire',
            old_name='area_unknown',
            new_name='initial_area_unknown',
        ),
        migrations.RemoveField(
            model_name='bushfire',
            name='fire_level',
        ),
        migrations.AddField(
            model_name='bushfire',
            name='initial_area',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Area of fire at arrival (ha)'),
        ),
        migrations.AddField(
            model_name='bushfire',
            name='max_fire_level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], null=True, verbose_name=b'Maximum fire level'),
        ),
        migrations.AddField(
            model_name='bushfire',
            name='prob_fire_level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], null=True, verbose_name=b'Probable fire level'),
        ),
    ]