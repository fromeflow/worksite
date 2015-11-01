# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20151005_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseversion',
            name='syllabus',
            field=models.FileField(verbose_name='Рабочая программа', null=True, upload_to=courses.models.UPLOAD_VERSION_SYLLABUS, blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='classwork',
            name='course_semester',
            field=models.ForeignKey(to='courses.CourseSemester', related_name='classwork_set', verbose_name='Семестр курса'),
        ),
    ]
