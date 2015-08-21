# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20150821_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='Пользователь'),
        ),
    ]
