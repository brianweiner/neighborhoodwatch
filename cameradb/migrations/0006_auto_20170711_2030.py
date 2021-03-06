# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cameradb', '0005_auto_20170711_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='camera',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cameradb.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cameradb.Profile'),
            preserve_default=False,
        ),
    ]
