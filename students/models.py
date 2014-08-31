from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import students


class Speciality(models.Model):
    code = models.CharField(verbose_name='Шифр', max_length=8)
    name = models.CharField(verbose_name='Название', max_length=100)
    specialization = models.CharField(verbose_name='Специализация', max_length=200,
                                      blank=True)
    type = models.CharField(verbose_name='Квалификация', max_length=1,
                            choices=(('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист')))
    standard_generation = models.IntegerField(verbose_name='Поколение стандарта', default=3,
                                              validators=[MinValueValidator(1), MaxValueValidator(9)])

    def __str__(self):
        return '{code} {name} [ФГОС-{standard}]'.format(
            code=self.code,
            name=self.name,
            standard=self.standard_generation
        )

    class Meta:
        ordering = ['code']
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
        unique_together = (('code', 'standard_generation', 'type'),)


class Group(models.Model):
    suffix = models.CharField(verbose_name='Суффикс специальности', max_length=2)
    speciality = models.ForeignKey(verbose_name='Специальность', to=Speciality)
    year = models.IntegerField(verbose_name='Год поступления',
                               validators=[MinValueValidator(1930), MaxValueValidator(2100)])
    max_course = models.IntegerField(verbose_name='Старший курс', default=4,
                                     validators=[MinValueValidator(1), MaxValueValidator(7)])
    code = models.CharField(max_length=10, verbose_name='Шифр', blank=True)
    distance_learning = models.BooleanField(verbose_name='Заочное обучение', default=False)

    # FIXME: Проверять, закончился ли учебный год (граница — июль)
    @property
    def name(self):
        finished = ''
        diff = datetime.now().year - self.year
        if diff > self.max_course:
            diff = self.max_course
            finished = '*'
        return '{course}{suffix}{finished}'.format(
            course=diff,
            suffix=self.suffix,
            finished=finished)

    @property
    def years(self):
        return "{begin}—{end}".format(
            begin=self.year,
            end=self.year + self.max_course
        )

    # FIXME: Добавить метаданные в класс и тэг to_link
    def to_link(self):
        return '<span class="{cls}"></span>&nbsp;<a href="{link}">{text}</a>' \
            .format(
            link=reverse(students.views.group_detail, kwargs={'group_id': self.id}),
            text=str(self),
            cls='text-muted fa-group'
        )

    def __str__(self):
        return '{name} (’{year})'.format(
            name=self.name,
            year=self.year + self.max_course
        )

    def get_absolute_url(self):
        return reverse('students-group-detail', kwargs={'group_id': self.id})

    class Meta:
        ordering = ['-year', 'suffix']
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        unique_together = (('code', 'year'),)


class Student(models.Model):
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    name = models.CharField(verbose_name='Имя', max_length=20,
                            blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=20,
                                  blank=True)
    sex = models.CharField(verbose_name="Пол", max_length=1,
                           choices=(('M', 'М'), ('F', 'Ж')))
    group = models.ForeignKey(to=Group, verbose_name="Группа")
    sent_down = models.BooleanField(verbose_name='Отчислен', default=False)
    user = models.OneToOneField(verbose_name='Связан с пользователем',
                                null=True, blank=True,
                                to=User,
                                default=None)

    @property
    def surname_initials(self):
        s = self.surname.capitalize()
        if self.name: s += ' {n}.'.format(n=self.name[0].upper())
        if self.patronymic: s += ' {p}.'.format(p=self.patronymic[0].upper())
        return s

    def to_link(self):
        return '<span class="{cls}"></span>&nbsp;<a href="{link}">{text}</a>' \
            .format(
            link=reverse('students-detail', kwargs={'pk': self.id}),
            text=self.surname_initials,
            cls='text-muted glyphicon glyphicon-user'
        )

    def __str__(self):
        s = self.surname_initials
        s += ' [{group}]'.format(group=self.group)
        return s

    def get_absolute_url(self):
        return reverse('students-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['group', 'surname']
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
