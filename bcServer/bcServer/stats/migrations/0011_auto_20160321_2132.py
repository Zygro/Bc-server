# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_auto_20160321_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonstat',
            old_name='lessonID',
            new_name='lesson',
        ),
    ]
