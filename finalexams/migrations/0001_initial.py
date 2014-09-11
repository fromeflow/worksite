# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import finalexams.models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finalexam',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Название экзамена', max_length=100)),
                ('date', models.DateTimeField(verbose_name='Дата проведения', null=True, blank=True)),
                ('questions', models.FileField(verbose_name='Вопросы', null=True, upload_to=finalexams.models.UPLOAD_TO,
                                               blank=True)),
                ('group', models.ForeignKey(to='students.Group', verbose_name='Группа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
