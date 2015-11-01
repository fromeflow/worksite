# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_group_max_level'),
        ('courses', '0021_auto_20151101_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseversion',
            options={'verbose_name_plural': 'версии дисциплин', 'ordering': ['group', 'course'], 'verbose_name': 'версия дисциплины'},
        ),
        migrations.AddField(
            model_name='courseversion',
            name='group',
            field=models.ForeignKey(null=True, default=None, blank=True, to='students.Group', verbose_name='Группа'),
        ),
        migrations.AlterUniqueTogether(
            name='courseversion',
            unique_together=set([('course', 'group')]),
        ),
        migrations.RemoveField(
            model_name='courseversion',
            name='version',
        ),
    ]
