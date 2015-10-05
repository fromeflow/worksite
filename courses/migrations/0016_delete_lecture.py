# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20151005_1846'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
