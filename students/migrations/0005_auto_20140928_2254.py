# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0004_auto_20140928_2234'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('suffix', 'entrance_year'), ('code', 'entrance_year')]),
        ),
    ]
