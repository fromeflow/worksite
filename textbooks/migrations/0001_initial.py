# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators

import textbooks.models


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('authors', models.CharField(verbose_name='Авторы', max_length=200, default='Великодный В. И.')),
                ('compiler', models.BooleanField(verbose_name='Составитель', default=True)),
                ('title', models.CharField(verbose_name='Название', max_length=200)),
                ('publisher', models.CharField(verbose_name='Издательство', blank=True, null=True, max_length=100)),
                ('year', models.IntegerField(validators=[
                    [django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2100)]],
                                             verbose_name='Год издания', blank=True, null=True)),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('course',
                 models.ManyToManyField(to='courses.Course', verbose_name='Дисциплина', blank=True, null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'пособия',
                'verbose_name': 'пособие',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextbookMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Название', max_length=100)),
                ('file', models.FileField(verbose_name='Материалы', upload_to=textbooks.models.UPLOAD_TO)),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('textbook', models.ForeignKey(to='textbooks.Textbook', verbose_name='Пособие')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'материал пособия',
                'verbose_name_plural': 'материалы пособия',
            },
            bases=(models.Model,),
        ),
        migrations.AlterOrderWithRespectTo(
            name='textbookmaterial',
            order_with_respect_to='textbook',
        ),
        migrations.AlterUniqueTogether(
            name='textbook',
            unique_together=set([('title',)]),
        ),
    ]
