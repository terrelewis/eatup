# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plateup', '0009_auto_20160404_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='picture',
        ),
    ]
