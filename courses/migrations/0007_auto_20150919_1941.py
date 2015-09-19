# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150919_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'дисциплина', 'ordering': ['specialty', 'title'], 'verbose_name_plural': 'дисциплины'},
        ),
        migrations.AlterModelOptions(
            name='coursesemester',
            options={'verbose_name': 'семестр курса', 'ordering': ['course_version', 'number'], 'verbose_name_plural': 'семестры курсов'},
        ),
        migrations.AlterModelOptions(
            name='courseversion',
            options={'verbose_name': 'версия дисциплины', 'ordering': ['version'], 'verbose_name_plural': 'версии дисциплин'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'экзамен/зачёт', 'ordering': ['course_semester'], 'verbose_name_plural': 'экзамены/зачёты'},
        ),
        migrations.AlterModelOptions(
            name='lecture',
            options={'verbose_name': 'лекция', 'ordering': ['course_semester', 'number'], 'verbose_name_plural': 'лекции'},
        ),
    ]
