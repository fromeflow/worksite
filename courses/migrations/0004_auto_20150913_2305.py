# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150913_2301'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coursesemester',
            unique_together=set([('course_version', 'number')]),
        ),
    ]
