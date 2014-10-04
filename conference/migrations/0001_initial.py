# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators

import conference.models
import misc.model_mixins


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0006_auto_20141002_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Тема', max_length=100)),
                ('description', models.TextField(verbose_name='Описание работы', blank=True)),
                ('section', models.CharField(verbose_name='Секция', max_length=50, blank=True)),
                ('place', models.IntegerField(validators=[django.core.validators.MinValueValidator(1),
                                                          django.core.validators.MaxValueValidator(3)],
                                              verbose_name='Место', blank=True, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1930),
                                                         django.core.validators.MaxValueValidator(2100)],
                                             verbose_name='Учебный год')),
                ('student', models.ForeignKey(to='students.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name_plural': 'доклады',
                'verbose_name': 'доклад',
                'ordering': ['-year', 'title'],
            },
            bases=(models.Model, misc.model_mixins.ToLinkMixin),
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=100)),
                ('file', models.FileField(verbose_name='Материалы', upload_to=conference.models.UPLOAD_TO)),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('report', models.ForeignKey(to='conference.Report', verbose_name='Доклад')),
            ],
            options={
                'verbose_name_plural': 'материалы доклада',
                'verbose_name': 'материал доклада',
                'ordering': ['report'],
            },
            bases=(models.Model,),
        ),
    ]
