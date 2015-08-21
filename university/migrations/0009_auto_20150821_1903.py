# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_auto_20150821_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='specialization',
            field=models.CharField(verbose_name='Профиль (специализация)', blank=True, max_length=200),
        ),
    ]
