# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150911_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericproject',
            name='materials',
            field=models.FileField(blank=True, upload_to=projects.models.UPLOAD_PROJECT_MATERIALS, max_length=150, null=True, verbose_name='Материалы'),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='slides',
            field=models.FileField(blank=True, upload_to=projects.models.UPLOAD_PROJECT_SLIDES, max_length=150, null=True, verbose_name='Слайды'),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='text',
            field=models.FileField(blank=True, upload_to=projects.models.UPLOAD_PROJECT_TEXT, max_length=150, null=True, verbose_name='Текст'),
        ),
    ]
