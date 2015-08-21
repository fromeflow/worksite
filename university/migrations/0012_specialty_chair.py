# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0011_auto_20150821_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='chair',
            field=models.ForeignKey(to='university.Chair', blank=True, null=True, verbose_name='Выпускающая кафедра'),
        ),
    ]
