# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150915_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abbreviation',
            field=models.CharField(max_length=20, verbose_name='Сокращённое название', db_index=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название курса'),
        ),
    ]
