# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_lesson_inputs'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
