# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models
import utils.mixins
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_group_max_level'),
        ('university', '0014_specialty_max_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Тема')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('mark', models.IntegerField(null=True, blank=True, verbose_name='Оценка', validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)], default=None)),
                ('completed', models.BooleanField(verbose_name='Завершена', default=False)),
                ('text', models.FileField(upload_to=projects.models.UPLOAD_PROJECT_TEXT, blank=True, verbose_name='Текст', null=True)),
                ('slides', models.FileField(upload_to=projects.models.UPLOAD_PROJECT_SLIDES, blank=True, verbose_name='Слайды', null=True)),
                ('materials', models.FileField(upload_to=projects.models.UPLOAD_PROJECT_MATERIALS, blank=True, verbose_name='Материалы', null=True)),
            ],
            options={
                'verbose_name_plural': 'студенческие работы',
                'verbose_name': 'студенческая работа',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CourseProject',
            fields=[
                ('genericproject_ptr', models.OneToOneField(to='projects.GenericProject', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('year', models.IntegerField(blank=True, verbose_name='Учебный год', validators=[django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2100)], null=True)),
                ('semester', models.CharField(null=True, blank=True, max_length=1, verbose_name='Семестр', choices=[('1', 1), ('2', 2)])),
            ],
            options={
                'verbose_name_plural': 'курсовые работы',
                'verbose_name': 'курсовая работа',
                'ordering': ['-year', 'student__surname'],
            },
            bases=(utils.mixins.ToLinkMixin, 'projects.genericproject'),
        ),
        migrations.CreateModel(
            name='FinalProject',
            fields=[
                ('genericproject_ptr', models.OneToOneField(to='projects.GenericProject', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
            ],
            options={
                'verbose_name_plural': 'квалификационные работы',
                'verbose_name': 'квалификационная работа',
                'ordering': ['student__group__graduation_year', 'student__surname'],
            },
            bases=(utils.mixins.ToLinkMixin, 'projects.genericproject'),
        ),
        migrations.AddField(
            model_name='genericproject',
            name='student',
            field=models.ForeignKey(to='students.Student', default=None, blank=True, null=True, verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='genericproject',
            name='supervisor',
            field=models.ForeignKey(to='university.Employee', default=None, blank=True, null=True, verbose_name='Руководитель'),
        ),
    ]
