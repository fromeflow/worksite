# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators

import courseworks.models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '__first__'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1930),
                                                                    django.core.validators.MaxValueValidator(2100)],
                                             blank=True, verbose_name='Учебный год')),
                ('semester',
                 models.CharField(blank=True, max_length=1, choices=[('1', 1), ('2', 2)], verbose_name='Семестр')),
                ('mark', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2),
                                                                    django.core.validators.MaxValueValidator(5)],
                                             blank=True, default=None, verbose_name='Оценка')),
                ('completed', models.BooleanField(default=False, verbose_name='Завершена')),
                ('slides', models.FileField(null=True, upload_to=courseworks.models.UPLOAD_TO_SLIDES, blank=True,
                                            verbose_name='Слайды')),
                ('text',
                 models.FileField(null=True, upload_to=courseworks.models.UPLOAD_TO, blank=True, verbose_name='Текст')),
                ('materials', models.FileField(null=True, upload_to=courseworks.models.UPLOAD_TO_MATERIALS, blank=True,
                                               verbose_name='Материалы')),
                ('course', models.ForeignKey(null=True, verbose_name='Дисциплина', blank=True, to='courses.Course')),
                ('student', models.ForeignKey(null=True, to='students.Student', verbose_name='Исполнитель', blank=True,
                                              default=None)),
            ],
            options={
                'verbose_name_plural': 'курсовые работы',
                'ordering': ['-year', 'student__surname'],
                'verbose_name': 'курсовая работа',
            },
            bases=(models.Model,),
        ),
    ]
