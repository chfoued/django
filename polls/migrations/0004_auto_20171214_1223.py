# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_merge_20171214_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='produit',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
    ]
