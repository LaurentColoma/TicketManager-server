# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-04 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('time_related', '0005_weeklyevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyEvent',
            fields=[
                ('timerelatedobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='time_related.TimeRelatedObject')),
                ('every_x_day', models.CharField(max_length=2, verbose_name='Every X Day')),
                ('every_x_month', models.CharField(max_length=2, verbose_name='Every X Month')),
            ],
            options={
                'abstract': False,
            },
            bases=('time_related.timerelatedobject',),
        ),
        migrations.CreateModel(
            name='YearlyEvent',
            fields=[
                ('timerelatedobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='time_related.TimeRelatedObject')),
                ('every_x_day', models.CharField(max_length=2, verbose_name='Every X Day')),
            ],
            options={
                'abstract': False,
            },
            bases=('time_related.timerelatedobject',),
        ),
        migrations.AddField(
            model_name='timerelatedobject',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_time_related.timerelatedobject_set+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='dailyevent',
            name='every_x_day',
            field=models.CharField(max_length=2, verbose_name='Every X day'),
        ),
    ]
