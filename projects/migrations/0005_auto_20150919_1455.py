# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.private_storage.storage
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150918_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericproject',
            name='materials',
            field=models.FileField(null=True, verbose_name='Материалы', max_length=150, upload_to=projects.models.UPLOAD_PROJECT_MATERIALS, blank=True, storage=utils.private_storage.storage.PrivateStorage()),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='slides',
            field=models.FileField(null=True, verbose_name='Слайды', max_length=150, upload_to=projects.models.UPLOAD_PROJECT_SLIDES, blank=True, storage=utils.private_storage.storage.PrivateStorage()),
        ),
        migrations.AlterField(
            model_name='genericproject',
            name='text',
            field=models.FileField(null=True, verbose_name='Текст', max_length=150, upload_to=projects.models.UPLOAD_PROJECT_TEXT, blank=True, storage=utils.private_storage.storage.PrivateStorage()),
        ),
    ]
