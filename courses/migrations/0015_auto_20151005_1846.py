# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20151005_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={},
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='course_semester',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='description',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='number',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='title',
        ),
    ]
