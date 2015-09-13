# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_group_max_level'),
        ('university', '0014_specialty_max_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название курса', max_length=100)),
                ('abbreviation', models.CharField(db_index=True, max_length=10, verbose_name='Сокращённое название')),
                ('closed', models.BooleanField(default=False, verbose_name='Не преподаётся')),
                ('description', models.TextField(verbose_name='Общее описание курса')),
                ('chair', models.ForeignKey(to='university.Chair', verbose_name='Кафедра')),
                ('specialty', models.ForeignKey(to='university.Specialty', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'дисциплина',
                'verbose_name_plural': 'дисциплины',
            },
        ),
        migrations.CreateModel(
            name='CourseSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер семестра', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(14)])),
            ],
            options={
                'verbose_name': 'семестр курса',
                'verbose_name_plural': 'семестры курсов',
            },
        ),
        migrations.CreateModel(
            name='CourseVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('version', models.PositiveSmallIntegerField(verbose_name='Номер версии', default=1)),
                ('version_description', models.TextField(blank=True, verbose_name='Описание версии курса')),
                ('lecture_time', models.PositiveSmallIntegerField(verbose_name='Лекционных часов')),
                ('practice_time', models.PositiveSmallIntegerField(verbose_name='Практических часов')),
                ('lab_time', models.PositiveSmallIntegerField(verbose_name='Лабораторных часов')),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'версия дисциплины',
                'verbose_name_plural': 'версии дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('exam_type', models.CharField(verbose_name='Вид контроля', choices=[('E', 'Экзамен'), ('T', 'Зачёт')], max_length=1)),
                ('course_semester', models.ForeignKey(to='courses.CourseSemester', verbose_name='Семестр курса')),
            ],
            options={
                'verbose_name': 'экзамен/зачёт',
                'verbose_name_plural': 'экзамены/зачёты',
            },
        ),
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, null=True, verbose_name='Оценка')),
                ('passed', models.BooleanField(default=False, verbose_name='Зачтено')),
                ('exam', models.ForeignKey(to='courses.Exam', verbose_name='Промежуточный контроль')),
                ('student', models.ForeignKey(to='students.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'экз. оценка',
                'verbose_name_plural': 'экз. оценка',
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(verbose_name='Тема', max_length=100)),
                ('course_semester', models.ForeignKey(to='courses.CourseSemester', verbose_name='Семестр курса')),
            ],
            options={
                'verbose_name': 'лекция',
                'verbose_name_plural': 'лекции',
            },
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='course_version',
            field=models.ForeignKey(to='courses.CourseVersion', verbose_name='Версия курса'),
        ),
        migrations.AlterUniqueTogether(
            name='courseversion',
            unique_together=set([('course', 'version')]),
        ),
    ]
