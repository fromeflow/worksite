# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

import seminars.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('speaker', models.CharField(max_length=50, verbose_name='Докладчик', blank=True)),
                ('date', models.DateTimeField(verbose_name='Дата проведения', blank=True, null=True)),
                ('venue', models.CharField(max_length=100, verbose_name='Место проведения', blank=True, null=True)),
                ('description', models.TextField(verbose_name='Описание семинара', blank=True)),
                ('speaker_user',
                 models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='Связанный пользователь',
                                   blank=True)),
            ],
            options={
                'verbose_name': 'семинар',
                'verbose_name_plural': 'семинары',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeminarFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('file', models.FileField(verbose_name='Материалы', upload_to=seminars.models.UPLOAD_TO)),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('seminar', models.ForeignKey(verbose_name='Семинар', to='seminars.Seminar')),
            ],
            options={
                'verbose_name': 'материал семинара',
                'verbose_name_plural': 'материалы семинара',
                'ordering': ['seminar'],
            },
            bases=(models.Model,),
        ),
    ]
