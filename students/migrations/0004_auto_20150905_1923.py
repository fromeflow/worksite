# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='supervisor',
            field=models.ForeignKey(to='university.Employee', verbose_name='Куратор', null=True, default=None, blank=True),
        ),
    ]
