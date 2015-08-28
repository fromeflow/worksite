# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='person_ptr',
            field=models.OneToOneField(parent_link=True, to='accounts.Person', auto_created=True, primary_key=True, serialize=False, default=None),
            preserve_default=False,
        ),
    ]
