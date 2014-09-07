# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('suffix', models.CharField(max_length=2, verbose_name='Суффикс специальности')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1930),
                                                         django.core.validators.MaxValueValidator(2100)],
                                             verbose_name='Год поступления')),
                ('max_course', models.IntegerField(validators=[django.core.validators.MinValueValidator(1),
                                                               django.core.validators.MaxValueValidator(7)], default=4,
                                                   verbose_name='Старший курс')),
                ('code', models.CharField(max_length=10, verbose_name='Шифр', blank=True)),
                ('distance_learning', models.BooleanField(default=False, verbose_name='Заочное обучение')),
            ],
            options={
                'verbose_name_plural': 'группы',
                'ordering': ['-year', 'suffix'],
                'verbose_name': 'группа',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name='Шифр')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('specialization', models.CharField(max_length=200, verbose_name='Специализация', blank=True)),
                ('type', models.CharField(max_length=1, verbose_name='Квалификация',
                                          choices=[('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист')])),
                ('standard_generation', models.IntegerField(validators=[django.core.validators.MinValueValidator(1),
                                                                        django.core.validators.MaxValueValidator(9)],
                                                            default=3, verbose_name='Поколение стандарта')),
            ],
            options={
                'verbose_name_plural': 'специальности',
                'ordering': ['code'],
                'verbose_name': 'специальность',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=20, verbose_name='Имя', blank=True)),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество', blank=True)),
                ('sex', models.CharField(max_length=1, verbose_name='Пол', choices=[('M', 'М'), ('F', 'Ж')])),
                ('sent_down', models.BooleanField(default=False, verbose_name='Отчислен')),
                ('group', models.ForeignKey(to='students.Group', verbose_name='Группа')),
                ('user',
                 models.OneToOneField(to=settings.AUTH_USER_MODEL, default=None, verbose_name='Связан с пользователем',
                                      blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'студенты',
                'ordering': ['group', 'surname'],
                'verbose_name': 'студент',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='speciality',
            unique_together=set([('code', 'standard_generation', 'type')]),
        ),
        migrations.AddField(
            model_name='group',
            name='speciality',
            field=models.ForeignKey(to='students.Speciality', verbose_name='Специальность'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('code', 'year')]),
        ),
    ]
