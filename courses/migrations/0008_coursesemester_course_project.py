# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20150919_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesemester',
            name='course_project',
            field=models.BooleanField(verbose_name='Курсовая работа', default=False),
        ),
    ]
