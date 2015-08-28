# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('university', '0012_specialty_chair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='person_ptr',
            field=models.OneToOneField(parent_link=True, to='accounts.Person', auto_created=True, primary_key=True, serialize=False, default=None),
            preserve_default=False,
        ),
    ]
