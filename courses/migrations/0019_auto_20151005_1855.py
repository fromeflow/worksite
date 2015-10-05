# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20151005_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturenew',
            name='classwork_ptr',
        ),
        migrations.DeleteModel(
            name='LectureNew',
        ),
    ]
