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
            name='Chair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название кафедры', max_length=50)),
                ('short_name', models.CharField(verbose_name='Сокращённое название', max_length=8)),
            ],
            options={
                'verbose_name': 'кафедра',
                'verbose_name_plural': 'кафедры',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('name', models.CharField(blank=True, verbose_name='Имя', max_length=20)),
                ('patronymic', models.CharField(blank=True, verbose_name='Отчество', max_length=20)),
                ('sex', models.CharField(verbose_name='Пол', choices=[('M', 'М'), ('F', 'Ж')], max_length=1)),
                ('position', models.CharField(blank=True, verbose_name='Должность', max_length=50)),
                ('degree', models.CharField(blank=True, verbose_name='Учёная степень', max_length=20)),
                ('chair', models.ForeignKey(to='university.Chair', verbose_name='Кафедра', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название факультета', max_length=50)),
                ('short_name', models.CharField(verbose_name='Сокращённое название', max_length=8)),
                ('dean', models.OneToOneField(to='university.Employee', verbose_name='Декан')),
            ],
            options={
                'verbose_name': 'факультет',
                'verbose_name_plural': 'факультеты',
            },
        ),
        migrations.AddField(
            model_name='chair',
            name='faculty',
            field=models.ForeignKey(verbose_name='Факультет', to='university.Faculty'),
        ),
    ]
