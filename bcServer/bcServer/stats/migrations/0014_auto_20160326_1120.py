# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-26 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0013_auto_20160324_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonstat',
            name='bad_solutions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lessonstat',
            name='good_solutions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]