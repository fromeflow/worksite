# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('chair', models.CharField(max_length=50, verbose_name='Название кафедры')),
            ],
            options={
                'verbose_name': 'кафедра',
                'verbose_name_plural': 'кафедры',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('closed', models.BooleanField(default=False, verbose_name='Не преподаётся')),
                ('chair', models.ForeignKey(to='courses.Chair', verbose_name='Кафедра')),
                ('speciality', models.ForeignKey(to='students.Speciality', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'дисциплина',
                'verbose_name_plural': 'дисциплины',
            },
            bases=(models.Model,),
        ),
    ]
