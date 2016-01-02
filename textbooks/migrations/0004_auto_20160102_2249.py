# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 20:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0003_auto_20151231_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbookfile',
            name='order',
            field=models.IntegerField(default=100, verbose_name='Позиция в списке'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1930), django.core.validators.MaxValueValidator(2100)], verbose_name='Год издания'),
        ),
    ]