# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0003_auto_20140927_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'специальности', 'ordering': ['standard_generation', 'code'],
                     'verbose_name': 'специальность'},
        ),
    ]
