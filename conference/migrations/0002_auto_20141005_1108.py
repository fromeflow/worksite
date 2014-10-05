# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0001_initial'),
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='section',
        ),
        migrations.AddField(
            model_name='report',
            name='chair',
            field=models.ForeignKey(verbose_name='Кафедра', to='courses.Chair', null=True),
            preserve_default=True,
        ),
    ]
