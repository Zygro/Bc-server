# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0018_auto_20160420_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='interactive',
            field=models.BooleanField(default=False),
        ),
    ]
