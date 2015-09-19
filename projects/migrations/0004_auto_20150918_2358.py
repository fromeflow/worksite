# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150913_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericproject',
            name='materials',
            field=models.FileField(null=True, upload_to=projects.models.UPLOAD_PROJECT_MATERIALS, storage=django.core.files.storage.FileSystemStorage(base_url='private/', location='/srv/worksite/private/'), max_length=150, verbose_name='Материалы', blank=True),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='slides',
            field=models.FileField(null=True, upload_to=projects.models.UPLOAD_PROJECT_SLIDES, storage=django.core.files.storage.FileSystemStorage(base_url='private/', location='/srv/worksite/private/'), max_length=150, verbose_name='Слайды', blank=True),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='text',
            field=models.FileField(null=True, upload_to=projects.models.UPLOAD_PROJECT_TEXT, storage=django.core.files.storage.FileSystemStorage(base_url='private/', location='/srv/worksite/private/'), max_length=150, verbose_name='Текст', blank=True),
        ),
    ]
