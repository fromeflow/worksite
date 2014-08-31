from django.db import models

from students.models import Speciality

class Chair(models.Model):
    chair = models.CharField(verbose_name='Название кафедры', max_length=50)

    def __str__(self):
        return self.chair

    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'

class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=100)
    chair = models.ForeignKey(verbose_name='Кафедра', to=Chair)
    speciality = models.ForeignKey(verbose_name='Специальность', to=Speciality)
    closed = models.BooleanField(verbose_name='Не преподаётся', default=False)

    def __str__(self):
        return "{title} ({speciality})".format(
            title=self.title,
            speciality=self.speciality
        )

    class Meta:
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'

        # # TODO сделать ссылку на него из coursework
        # class WorkYear:
#     year = None
#
# # TODO
        # Версия курса (меняется от года к году), привязана к конкретной группе
        # class CourseVersion:
#     work_year = None
#     course = None
        # group = ForeignKey
        #
# Один семестр данной версии курса. семестр — от 1 до 8(10)
        # class CourseSemester:
#     course_version = None
#     semester_number = None
        #     exam_form = None
#
# # TODO
# Одна лекционная тема
        # class Lecture:
#     course_semester = None
#     number = None
#     title = None
#
# # TODO
# Одна лабораторная работа
        # class LabWork:
#     course_semester = None
#     number = None
#     title = None
#     start_time = None
#     due = None
#     deadline = None
#
# # TODO
# class PracticeWork:
#     course_semester = None
#     number = None
#     title = None
#
# # TODO
# class IndividualWork:
#     course_semester = None
#     number = None
#     title = None
#
# # TODO
# class MarkLabWork:
#     student = None
#     lab_work = None
#     mark = None
#
# # TODO
# class MarkIndividualWork:
#     student = None
#     lab_work = None
#     mark = None
#
# # TODO
# class MarkPracticeWork:
#     student = None
#     lab_work = None
#     mark = None
#
# # TODO
# class Session:
#     student = None
#     course_semester = None
#     mark = None