# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_delete_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('classwork_ptr', models.OneToOneField(to='courses.ClassWork', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
            ],
            options={
                'verbose_name': 'лекция',
                'verbose_name_plural': 'лекции',
            },
            bases=('courses.classwork',),
        ),
    ]
