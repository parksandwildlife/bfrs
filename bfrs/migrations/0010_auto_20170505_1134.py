# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-05 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0009_snapshothistory_prev_snapshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bushfiretest',
            name='district',
        ),
        migrations.RemoveField(
            model_name='bushfiretest',
            name='region',
        ),
        migrations.RemoveField(
            model_name='bushfiretest2',
            name='district',
        ),
        migrations.RemoveField(
            model_name='bushfiretest2',
            name='init_authorised_by',
        ),
        migrations.RemoveField(
            model_name='bushfiretest2',
            name='region',
        ),
        migrations.DeleteModel(
            name='BushfireTest',
        ),
        migrations.DeleteModel(
            name='BushfireTest2',
        ),
    ]
