# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_lessonstat_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonstat',
            old_name='lesson',
            new_name='lessonID',
        ),
    ]
