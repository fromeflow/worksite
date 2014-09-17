# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-entrance_year', 'suffix'], 'verbose_name_plural': 'группы',
                     'verbose_name': 'группа'},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='year',
            new_name='entrance_year',
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('code', 'entrance_year')]),
        ),
    ]
