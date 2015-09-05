# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0013_auto_20150828_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='max_level',
            field=models.IntegerField(default=4, verbose_name='Старший курс', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]
