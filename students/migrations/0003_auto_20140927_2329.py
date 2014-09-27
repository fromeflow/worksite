# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0002_auto_20140917_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='max_course',
            new_name='max_level',
        ),
    ]
