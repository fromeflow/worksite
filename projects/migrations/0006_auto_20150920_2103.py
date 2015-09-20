# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20150919_1941'),
        ('projects', '0005_auto_20150919_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseproject',
            options={'ordering': ['-course_semester__course_version', '-course_semester', 'student__surname'], 'verbose_name_plural': 'курсовые работы', 'verbose_name': 'курсовая работа'},
        ),
        migrations.AlterModelOptions(
            name='finalproject',
            options={'ordering': ['student__group', 'student__surname', 'title'], 'verbose_name_plural': 'квалификационные работы', 'verbose_name': 'квалификационная работа'},
        ),
        migrations.RemoveField(
            model_name='courseproject',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='courseproject',
            name='year',
        ),
        migrations.AddField(
            model_name='courseproject',
            name='course_semester',
            field=models.ForeignKey(to='courses.CourseSemester', default=None, null=True, verbose_name='Семестр курса', blank=True),
        ),
    ]
