# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0012_specialty_chair'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(max_length=2, verbose_name='Суффикс специальности')),
                ('entrance_year', models.IntegerField(verbose_name='Год поступления', validators=[django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2100)])),
                ('max_level', models.IntegerField(default=4, verbose_name='Старший курс', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='Шифр')),
                ('distance_learning', models.BooleanField(default=False, verbose_name='Заочное обучение')),
                ('specialty', models.ForeignKey(to='university.Specialty', verbose_name='Специальность')),
            ],
            options={
                'verbose_name_plural': 'группы',
                'ordering': ['-entrance_year', 'suffix'],
                'verbose_name': 'группа',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=20, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('M', 'М'), ('F', 'Ж')], max_length=1, verbose_name='Пол')),
                ('sent_down', models.BooleanField(default=False, verbose_name='Отчислен')),
                ('group', models.ForeignKey(to='students.Group', verbose_name='Группа')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'студенты',
                'ordering': ['group', 'surname'],
                'verbose_name': 'студент',
            },
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('suffix', 'entrance_year')]),
        ),
    ]
