# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0007_auto_20160225_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('difficulty', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('fun', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
