# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_auto_20150821_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='specialization',
            field=models.CharField(max_length=200, verbose_name='Специализация/профиль', blank=True),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='type',
            field=models.CharField(choices=[('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист')], max_length=1, default='B', verbose_name='Квалификация'),
        ),
    ]
