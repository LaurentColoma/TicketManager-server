# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-04 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_related', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timerelatedobject',
            name='daily',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='timerelatedobject',
            name='monthly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timerelatedobject',
            name='weekly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timerelatedobject',
            name='yearly',
            field=models.BooleanField(default=False),
        ),
    ]
