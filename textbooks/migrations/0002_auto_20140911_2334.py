# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('textbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='compiler',
            field=models.BooleanField(verbose_name='Составитель', default=False),
        ),
    ]
