from django.db import models

from students.models import Speciality, Group, Student


EXAM_TYPE_CHOICES = (('E', 'Экзамен'), ('T', 'Зачёт'))


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


# Версия курса (меняется от года к году), привязана к конкретной группе
class CourseVersion(models.Model):
    course = models.ForeignKey(verbose_name='Курс',
                               to=Course)
    group = models.ForeignKey(verbose_name='Группа',
                              to=Group)
    # Рабочая программа, прочие материалы


# Один семестр данной версии курса. семестр — от 1 до 8(10)
class CourseSemester(models.Model):
    course_version = models.ForeignKey(verbose_name='Версия курса',
                                       to=CourseVersion)
    semester_number = models.IntegerField(verbose_name='Номер семестра')


# Экзамен/зачёт
class Exam(models.Model):
    course_semester = models.ForeignKey(verbose_name='Версия курса',
                                        to=CourseSemester)
    exam_type = models.CharField(verbose_name='Вид контроля',
                                 max_length=1,
                                 choices=EXAM_TYPE_CHOICES)
    # вопросы к экзамену, билеты


class ExamMark(models.Model):
    student = models.ForeignKey(verbose_name='Студент',
                                to=Student)
    exam = models.ForeignKey(verbose_name='Промежуточный контроль',
                             to=Exam)
    mark = models.IntegerField(verbose_name='Оценка',
                               blank=True, null=True)
    passed = models.BooleanField(verbose_name='Зачтено',
                                 default=False)


class Lecture(models.Model):
    course_semester = models.ForeignKey(verbose_name='Семестр курса',
                                        to=CourseSemester)
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(verbose_name='Тема',
                             max_length=100)


# class StudentWork(models.Model):
# type = Home|Practice|Lab
#     course_semester = None
#     number = None
#     title = None
#     start_time = None
#     due = None
#     deadline = None
#
#
# class StudentWorkMark:
#     student = None
#     work = None
#     mark = None
