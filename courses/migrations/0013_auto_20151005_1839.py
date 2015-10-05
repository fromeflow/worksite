# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_lecture_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassWork',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('description', models.TextField(blank=True, verbose_name='Заметки к занятию')),
            ],
            options={
                'verbose_name': 'занятие',
                'verbose_name_plural': 'занятия',
                'ordering': ['course_semester', 'number'],
            },
        ),
        migrations.CreateModel(
            name='LabWork',
            fields=[
                ('classwork_ptr', models.OneToOneField(to='courses.ClassWork', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'лабораторные работы',
                'verbose_name': 'лабораторная работа',
            },
            bases=('courses.classwork',),
        ),
        migrations.CreateModel(
            name='LectureNew',
            fields=[
                ('classwork_ptr', models.OneToOneField(to='courses.ClassWork', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'лекции',
                'verbose_name': 'лекция',
            },
            bases=('courses.classwork',),
        ),
        migrations.CreateModel(
            name='PracticeWork',
            fields=[
                ('classwork_ptr', models.OneToOneField(to='courses.ClassWork', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'практическое занятие',
                'verbose_name': 'практическое занятие',
            },
            bases=('courses.classwork',),
        ),
        migrations.AddField(
            model_name='classwork',
            name='course_semester',
            field=models.ForeignKey(to='courses.CourseSemester', verbose_name='Семестр курса'),
        ),
    ]
