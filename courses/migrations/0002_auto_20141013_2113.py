# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0007_auto_20141006_1007'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSemester',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('semester_number', models.IntegerField(verbose_name='Номер семестра')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseVersion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('course', models.ForeignKey(verbose_name='Курс', to='courses.Course')),
                ('group', models.ForeignKey(verbose_name='Группа', to='students.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('exam_type', models.CharField(max_length=1, verbose_name='Вид контроля',
                                               choices=[('E', 'Экзамен'), ('T', 'Зачёт')])),
                ('course_semester', models.ForeignKey(verbose_name='Версия курса', to='courses.CourseSemester')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mark', models.IntegerField(null=True, verbose_name='Оценка', blank=True)),
                ('passed', models.BooleanField(verbose_name='Зачтено', default=False)),
                ('exam', models.ForeignKey(verbose_name='Промежуточный контроль', to='courses.Exam')),
                ('student', models.ForeignKey(verbose_name='Студент', to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('course_semester', models.ForeignKey(verbose_name='Семестр курса', to='courses.CourseSemester')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='course_version',
            field=models.ForeignKey(verbose_name='Версия курса', to='courses.CourseVersion'),
            preserve_default=True,
        ),
    ]
