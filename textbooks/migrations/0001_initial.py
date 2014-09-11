# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings

import textbooks.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=50)),
                ('name', models.CharField(verbose_name='Имя', max_length=20)),
                ('patronymic', models.CharField(verbose_name='Отчество', max_length=20)),
            ],
            options={
                'ordering': ['surname', 'name', 'patronymic'],
                'verbose_name_plural': 'авторы',
                'verbose_name': 'автор',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=200)),
                ('publisher', models.CharField(verbose_name='Издательство', null=True, blank=True, max_length=100)),
                ('year', models.IntegerField(verbose_name='Год издания', null=True, blank=True, validators=[
                    [django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2100)]])),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('course',
                 models.ManyToManyField(to='courses.Course', verbose_name='Дисциплина', null=True, blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'пособие',
                'verbose_name_plural': 'пособия',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextbookMaterial',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=100)),
                ('file', models.FileField(upload_to=textbooks.models.UPLOAD_TO, verbose_name='Материалы')),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('textbook', models.ForeignKey(verbose_name='Пособие', to='textbooks.Textbook')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'материалы семинара',
                'verbose_name': 'материал семинара',
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
        migrations.AddField(
            model_name='author',
            name='textbooks',
            field=models.ManyToManyField(verbose_name='Авторы', to='textbooks.Textbook'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(null=True, verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterOrderWithRespectTo(
            name='author',
            order_with_respect_to='textbooks',
        ),
    ]
