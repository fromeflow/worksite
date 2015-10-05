# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_courseversion_version_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.TextField(blank=True, verbose_name='Заметки к лекции'),
        ),
    ]
