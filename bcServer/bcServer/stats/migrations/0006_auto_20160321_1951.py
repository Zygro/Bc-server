# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20160321_1023'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([]),
        ),
    ]
