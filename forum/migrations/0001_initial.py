# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('post_date', models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now)),
                ('creator', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ['theme', '-post_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Тема', max_length=50)),
                ('creation_date', models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime.now)),
                ('creator', models.ForeignKey(verbose_name='Создатель', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'тема',
                'verbose_name_plural': 'темы',
                'ordering': ['-creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='theme',
            field=models.ForeignKey(verbose_name='Связанная тема', to='forum.Theme'),
            preserve_default=True,
        ),
    ]
