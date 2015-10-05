# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_data(apps, schema_editor):
    CourseVersion = apps.get_model("courses", "CourseVersion")
    for cv in CourseVersion.objects.all():
        cv.description = cv.version_description
        cv.save()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_courseversion_description'),
    ]

    operations = [
        migrations.RunPython(move_data),
    ]
