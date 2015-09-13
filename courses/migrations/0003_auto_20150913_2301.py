# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150913_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammark',
            name='mark',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Оценка'),
        ),
    ]
