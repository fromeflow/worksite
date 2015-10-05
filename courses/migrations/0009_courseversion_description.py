# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_coursesemester_course_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseversion',
            name='description',
            field=models.TextField(verbose_name='Описание версии курса', blank=True),
        ),
    ]
