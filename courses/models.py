from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse_lazy

from utils.mixins import ToLinkMixin

from university.models import Specialty, Chair
from students.models import Student


EXAM_TYPE_CHOICES = (('E', 'Экзамен'), ('T', 'Зачёт'))


class Course(ToLinkMixin, models.Model):
    'Курс'
    title = models.CharField(verbose_name='Название курса',max_length=200)
    abbreviation = models.CharField(verbose_name='Сокращённое название', max_length=20, db_index=True)
    specialty = models.ForeignKey(to=Specialty, verbose_name='Специальность')
    chair = models.ForeignKey(to=Chair, verbose_name='Кафедра')
    closed = models.BooleanField(verbose_name='Не преподаётся', default=False)
    description = models.TextField(verbose_name="Общее описание курса", blank=True)

    @property
    def version_numbers(self):
        return CourseVersion.objects.filter(course=self.id).values('id', 'version')

    @property
    def last_version(self):
        try:
            return CourseVersion.objects.filter(course=self.id)\
                .select_related('course').latest('version')
        except CourseVersion.DoesNotExist:
            return None

    def __str__(self):
        return "{title} ({specialty})".format(
            title=self.title,
            specialty=self.specialty
        )

    def get_absolute_url(self):
        return reverse_lazy('courses:course-last-version-redirect', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'
        ordering = ['specialty', 'title']

    def link_str(self):
        return self.title


class CourseVersion(models.Model):
    'Версия курса'
    course = models.ForeignKey(to=Course, verbose_name='Курс')
    version = models.PositiveSmallIntegerField(verbose_name='Номер версии', default=1)
    version_description = models.TextField(verbose_name='Описание версии курса', blank=True)
    # рабочая программа, материалы

    def get_absolute_url(self):
        return reverse_lazy('courses:course-version-detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{course} - {version}".format(
            course=self.course,
            version=self.version
        )

    class Meta:
        verbose_name = 'версия дисциплины'
        verbose_name_plural = 'версии дисциплин'
        unique_together = (('course', 'version'),)
        ordering = ['version']

    def link_str(self):
        return self.title


class CourseSemester(models.Model):
    'Один семестр курса'
    course_version = models.ForeignKey(to=CourseVersion, verbose_name='Версия курса')
    number = models.PositiveSmallIntegerField(verbose_name='Номер семестра',
                                      validators=[MinValueValidator(1), MaxValueValidator(14)])
    lecture_time = models.PositiveSmallIntegerField(verbose_name='Лекционных часов', default=0)
    practice_time = models.PositiveSmallIntegerField(verbose_name='Практических часов', default=0)
    lab_time = models.PositiveSmallIntegerField(verbose_name='Лабораторных часов', default=0)

    def __str__(self):
        return "{course_version} / {number}".format(
            course_version=self.course_version,
            number=self.number
        )

    class Meta:
        verbose_name = 'семестр курса'
        verbose_name_plural = 'семестры курсов'
        unique_together = (('course_version', 'number'),)
        ordering = ['course_version', 'number']

class Exam(models.Model):
    'Экзамен/зачёт'
    course_semester = models.ForeignKey(to=CourseSemester, verbose_name='Семестр курса')
    exam_type = models.CharField(verbose_name='Вид контроля', max_length=1,
                                 choices=EXAM_TYPE_CHOICES)
    # вопросы к экзамену, билеты

    def __str__(self):
        return "{course_semester} [контроль]".format(
            course_semester=self.course_semester
        )

    class Meta:
        verbose_name = 'экзамен/зачёт'
        verbose_name_plural = 'экзамены/зачёты'
        ordering = ['course_semester']


class ExamMark(models.Model):
    exam = models.ForeignKey(to=Exam, verbose_name='Промежуточный контроль')
    student = models.ForeignKey(to=Student, verbose_name='Студент')
    mark = models.PositiveIntegerField(verbose_name='Оценка', blank=True, null=True)
    passed = models.BooleanField(verbose_name='Зачтено', default=False)

    def __str__(self):
        return "Экз. оценка ({student})".format(
            student=self.student
        )

    class Meta:
        verbose_name = 'экз. оценка'
        verbose_name_plural = 'экз. оценка'


class Lecture(models.Model):
    course_semester = models.ForeignKey(to=CourseSemester, verbose_name='Семестр курса')
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(verbose_name='Тема',
                             max_length=100)

    def __str__(self):
        return "Лекция: {course_semester}".format(
            course_semester=self.course_semester
        )

    class Meta:
        verbose_name = 'лекция'
        verbose_name_plural = 'лекции'
        ordering = ['course_semester', 'number']

## Вынести в отдельное приложение?
# class LabWork(models.Model):
#     pass
#
# class PracticeWork(models.Work):
#     pass
#
# class StudentWork(models.Model):
# # type = Home|Practice|Lab
#     course_semester = None
#     number = None
#     title = None
#     start_time = None
#     due = None
#     deadline = None
#
# class StudentWorkMark(models.Model):
#     student = None
#     work = None
#     mark = None