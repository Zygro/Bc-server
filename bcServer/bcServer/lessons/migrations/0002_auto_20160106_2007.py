# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
