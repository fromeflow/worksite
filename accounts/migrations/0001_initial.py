# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('name', models.CharField(verbose_name='Имя', blank=True, max_length=20)),
                ('patronymic', models.CharField(verbose_name='Отчество', blank=True, max_length=20)),
                ('sex', models.CharField(verbose_name='Пол', choices=[('M', 'М'), ('F', 'Ж')], max_length=1)),
                ('user', models.OneToOneField(verbose_name='Пользователь', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['surname'],
                'verbose_name': 'человек',
                'verbose_name_plural': 'люди',
            },
        ),
    ]
