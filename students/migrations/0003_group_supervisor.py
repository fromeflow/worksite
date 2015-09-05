# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0013_auto_20150828_1924'),
        ('students', '0002_auto_20150828_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='supervisor',
            field=models.ForeignKey(verbose_name='Куратор', null=True, default=None, to='university.Employee'),
        ),
    ]
