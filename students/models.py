from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from misc.model_mixins import ToLinkMixin
from misc.validators import year_validator, level_validator


SPECIALITY_TYPE_CHOICES = (('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист'))
SEX_CHOICES = (('M', 'М'), ('F', 'Ж'))


class Speciality(models.Model):
    "Специальность"
    code = models.CharField(
        verbose_name='Шифр',
        max_length=8)
    name = models.CharField(
        verbose_name='Название',
        max_length=100)
    specialization = models.CharField(
        verbose_name='Специализация',
        max_length=200,
        blank=True)
    type = models.CharField(
        verbose_name='Квалификация',
        max_length=1,
        choices=SPECIALITY_TYPE_CHOICES)
    standard_generation = models.IntegerField(
        verbose_name='Поколение стандарта',
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(9)])

    def __str__(self):
        return '{code} {name} [ФГОС-{standard}]'.format(
            code=self.code,
            name=self.name,
            standard=self.standard_generation
        )

    class Meta:
        ordering = ['-standard_generation', 'code']
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
        unique_together = (('code', 'standard_generation', 'type'),)


class Group(models.Model, ToLinkMixin):
    "Академическая группа"
    suffix = models.CharField(
        verbose_name='Суффикс специальности',
        max_length=2)
    speciality = models.ForeignKey(
        verbose_name='Специальность',
        to=Speciality)
    entrance_year = models.IntegerField(
        verbose_name='Год поступления',
        validators=year_validator)
    max_level = models.IntegerField(
        verbose_name='Старший курс',
        default=4,
        validators=level_validator)
    code = models.CharField(
        verbose_name='Шифр',
        max_length=10,
        blank=True)
    distance_learning = models.BooleanField(
        verbose_name='Заочное обучение',
        default=False)

    @property
    def level(self):
        diff = datetime.now().year - self.entrance_year
        month = datetime.now().month
        return diff if month <= 6 else diff + 1

    @property
    def name(self):
        return '{level}{suffix}'.format(
            level=min(self.level, self.max_level),
            suffix=self.suffix)

    @property
    def years(self):
        return "{begin}—{end}".format(
            begin=self.entrance_year,
            end=self.graduation_year
        )

    @property
    def graduation_year(self):
        return self.entrance_year + self.max_level

    @property
    def finished(self):
        return self.level > self.max_level

    link_icon_class = 'fa fa-group'

    def link_str(self):
        return 'Группа {name}'.format(
            name=self.name
        )

    def __str__(self):
        name = self.name
        if self.level > self.max_level:
            name += ' (’{year})'.format(
                name=self.name,
                year=self.entrance_year + self.max_level
            )
        return name

    def get_absolute_url(self):
        return reverse('students-group-detail', kwargs={'group_id': self.id})

    class Meta:
        ordering = ['-entrance_year', 'suffix']
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        unique_together = (('suffix', 'entrance_year'),)


class Student(models.Model, ToLinkMixin):
    "Студент"
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=20)
    name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        blank=True)
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=20,
        blank=True)
    sex = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=SEX_CHOICES)
    group = models.ForeignKey(
        verbose_name="Группа",
        to=Group)
    sent_down = models.BooleanField(
        verbose_name='Отчислен',
        default=False)
    user = models.OneToOneField(
        verbose_name='Связан с пользователем',
        to=User,
        blank=True, null=True,
        default=None)

    @property
    def surname_initials(self):
        s = self.surname.capitalize()
        if self.name: s += ' {n}.'.format(n=self.name[0].upper())
        if self.patronymic: s += ' {p}.'.format(p=self.patronymic[0].upper())
        return s

    link_icon_class = 'glyphicon glyphicon-user'

    def link_icon_str(self):
        return self.surname_initials

    def __str__(self):
        s = self.surname_initials
        s += ' [{group}]'.format(group=self.group)
        return s

    def get_absolute_url(self):
        return reverse('students-detail', kwargs={'student_id': self.id})

    class Meta:
        ordering = ['group', 'surname']
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
