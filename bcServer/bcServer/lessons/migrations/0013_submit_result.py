# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_remove_submit_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
