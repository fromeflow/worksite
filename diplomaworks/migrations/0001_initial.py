# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators

import diplomaworks.models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiplomaWork',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Тема', max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1930),
                                                         django.core.validators.MaxValueValidator(2100)],
                                             verbose_name='Учебный год', blank=True, null=True)),
                ('mark', models.IntegerField(validators=[django.core.validators.MinValueValidator(2),
                                                         django.core.validators.MaxValueValidator(5)],
                                             verbose_name='Оценка', blank=True, null=True, default=None)),
                ('completed', models.BooleanField(verbose_name='Завершена', default=False)),
                ('slides', models.FileField(blank=True, verbose_name='Слайды', null=True,
                                            upload_to=diplomaworks.models.UPLOAD_TO_SLIDES)),
                ('text', models.FileField(blank=True, verbose_name='Текст', null=True,
                                          upload_to=diplomaworks.models.UPLOAD_TO)),
                ('review', models.FileField(blank=True, verbose_name='Отзыв руководителя', null=True,
                                            upload_to=diplomaworks.models.UPLOAD_TO_REVIEW)),
                ('review_external', models.FileField(blank=True, verbose_name='Внешняя рецензия', null=True,
                                                     upload_to=diplomaworks.models.UPLOAD_TO_REVIEW_EXTERNAL)),
                ('materials', models.FileField(blank=True, verbose_name='Материалы', null=True,
                                               upload_to=diplomaworks.models.UPLOAD_TO_MATERIALS)),
                ('student', models.ForeignKey(verbose_name='Исполнитель', null=True, to='students.Student', blank=True,
                                              default=None)),
            ],
            options={
                'verbose_name': 'квалификационная работа',
                'ordering': ['-year', 'student__surname'],
                'verbose_name_plural': 'квалификационные работы',
            },
            bases=(models.Model,),
        ),
    ]
