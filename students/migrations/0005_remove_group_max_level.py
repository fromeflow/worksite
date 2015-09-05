# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150905_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='max_level',
        ),
    ]
