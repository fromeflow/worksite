# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20151005_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practicework',
            options={'verbose_name': 'практическое занятие', 'verbose_name_plural': 'практические занятия'},
        ),
    ]
