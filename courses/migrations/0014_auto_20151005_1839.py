# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_data(apps, schema_editor):
    Lecture = apps.get_model("courses", "Lecture")
    LectureNew = apps.get_model("courses", "LectureNew")
    for l in Lecture.objects.all():
        ln = LectureNew(
            course_semester=l.course_semester,
            number=l.number,
            title=l.title,
            description=l.description
        )
        ln.save()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20151005_1839'),
    ]

    operations = [
        migrations.RunPython(move_data),
    ]
