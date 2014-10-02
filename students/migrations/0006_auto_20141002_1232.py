# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0005_auto_20140928_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['-standard_generation', 'code'], 'verbose_name': 'специальность',
                     'verbose_name_plural': 'специальности'},
        ),
    ]
