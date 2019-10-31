# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-05-08 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0019_auto_20190508_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenure',
            name='report_group_order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Tenure category report group order in annual report'),
        ),
        migrations.AlterField(
            model_name='tenure',
            name='report_order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Tenure category order in annual report'),
        ),
    ]
