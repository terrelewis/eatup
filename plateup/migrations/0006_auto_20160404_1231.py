# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateup', '0005_auto_20160404_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='user',
            name='restaurant',
            field=models.ManyToManyField(to='plateup.Restaurant'),
        ),
    ]
