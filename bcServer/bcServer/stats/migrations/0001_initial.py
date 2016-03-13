# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
        ),
    ]
