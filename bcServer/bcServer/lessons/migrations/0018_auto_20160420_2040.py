# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-20 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0017_hint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='result',
            field=models.CharField(max_length=200),
        ),
    ]