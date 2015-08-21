# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='dean',
            field=models.OneToOneField(null=True, verbose_name='Декан', to='university.Employee'),
        ),
    ]
