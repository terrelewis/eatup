# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateup', '0006_auto_20160404_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='restaurant',
            field=models.ManyToManyField(default=1, to='plateup.Restaurant'),
        ),
    ]
