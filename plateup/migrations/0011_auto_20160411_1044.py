# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 10:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plateup', '0010_remove_restaurant_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('N/A', 'not defined')], default='not defined', max_length=15)),
                ('age', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='restaurant',
            field=models.ManyToManyField(blank=True, related_name='users', to='plateup.Restaurant'),
        ),
    ]
