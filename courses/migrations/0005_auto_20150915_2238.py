# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150913_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseversion',
            name='lab_time',
        ),
        migrations.RemoveField(
            model_name='courseversion',
            name='lecture_time',
        ),
        migrations.RemoveField(
            model_name='courseversion',
            name='practice_time',
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='lab_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Лабораторных часов'),
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='lecture_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Лекционных часов'),
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='practice_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Практических часов'),
        ),
    ]
