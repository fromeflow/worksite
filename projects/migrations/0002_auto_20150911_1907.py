# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finalproject',
            options={'verbose_name_plural': 'квалификационные работы', 'verbose_name': 'квалификационная работа', 'ordering': ['student__group', 'student__surname']},
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Тема'),
        ),
    ]
