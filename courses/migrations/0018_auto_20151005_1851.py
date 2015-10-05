# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_data(apps, schema_editor):
    Lecture = apps.get_model("courses", "Lecture")
    LectureNew = apps.get_model("courses", "LectureNew")
    for ln in LectureNew.objects.all():
        l = Lecture(
            course_semester=ln.course_semester,
            number=ln.number,
            title=ln.title,
            description=ln.description
        )
        l.save()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_lecture'),
    ]

    operations = [
        migrations.RunPython(move_data),
    ]
