# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150920_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genericproject',
            name='completed',
        ),
    ]
