# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_auto_20150821_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='specialization',
            field=models.CharField(verbose_name='Профиль (специализ.)', max_length=200, blank=True),
        ),
    ]
