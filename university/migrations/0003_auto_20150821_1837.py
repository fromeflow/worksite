# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20150821_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='chair',
            field=models.ForeignKey(verbose_name='Кафедра', blank=True, null=True, to='university.Chair'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dean',
            field=models.OneToOneField(verbose_name='Декан', blank=True, null=True, to='university.Employee'),
        ),
    ]
