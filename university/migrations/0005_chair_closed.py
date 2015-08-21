# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20150821_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='chair',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Закрыта'),
        ),
    ]
