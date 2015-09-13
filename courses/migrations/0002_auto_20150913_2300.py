# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseversion',
            options={'verbose_name_plural': 'версии дисциплин', 'verbose_name': 'версия дисциплины'},
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Общее описание курса', blank=True),
        ),
    ]
