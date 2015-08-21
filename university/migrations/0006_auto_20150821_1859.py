# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_chair_closed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Шифр')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('specialization', models.CharField(max_length=200, blank=True, verbose_name='Специализация/профиль')),
                ('type', models.CharField(choices=[('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист')], max_length=1, verbose_name='Квалификация')),
                ('term_level_1', models.CharField(choices=[('S', ('Специальность', 'Специализация')), ('D', ('Направление', 'Профиль'))], max_length=1, verbose_name='Термин')),
                ('standard_generation', models.CharField(default='3', max_length=2, validators=[django.core.validators.MinValueValidator('1'), django.core.validators.MaxValueValidator('9')], verbose_name='Поколение стандарта')),
            ],
            options={
                'verbose_name': 'специальность',
                'verbose_name_plural': 'специальности',
                'ordering': ['-standard_generation', 'code'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='specialty',
            unique_together=set([('code', 'standard_generation', 'type')]),
        ),
    ]
