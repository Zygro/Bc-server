# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_lesson_inputs'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0003_userstat'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_LessonStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
