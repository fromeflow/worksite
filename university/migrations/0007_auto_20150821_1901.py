# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_auto_20150821_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='term_level_1',
        ),
        migrations.AddField(
            model_name='specialty',
            name='term',
            field=models.CharField(choices=[('S', 'Специальность|Специализация'), ('D', 'Направление|Профиль')], default='D', max_length=1, verbose_name='Термин'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialization',
            field=models.CharField(default='B', max_length=200, verbose_name='Специализация/профиль'),
        ),
    ]
