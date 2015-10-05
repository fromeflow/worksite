# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20151005_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseversion',
            name='version_description',
        ),
    ]
