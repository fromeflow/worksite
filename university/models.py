from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Person
from utils.validators import year_validator, level_validator


SPECIALTY_TYPE_CHOICES = (('B', 'Бакалавр'), ('M', 'Магистр'), ('S', 'Специалист'))
SPECIALTY_TERM_CHOICES = (('S', 'Специальность|Специализация'), ('D', 'Направление|Профиль'))

class Faculty(models.Model):
    "Факультет"
    name = models.CharField(
        verbose_name='Название факультета',
        max_length=50)
    short_name = models.CharField(
        verbose_name='Сокращённое название',
        max_length=8)
    dean = models.OneToOneField('Employee',
        verbose_name='Декан',
        blank=True,
        null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'факультет'
        verbose_name_plural = 'факультеты'


class Chair(models.Model):
    "Кафедра"
    name = models.CharField(
        verbose_name='Название кафедры',
        max_length=50)
    short_name = models.CharField(
        verbose_name='Сокращённое название',
        max_length=8)
    faculty = models.ForeignKey(Faculty,
        verbose_name='Факультет')
    closed = models.BooleanField(
        verbose_name='Закрыта',
        default=False)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.faculty.short_name)

    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'

class Specialty(models.Model):
    "Специальность/направление"
    code = models.CharField(
        verbose_name='Шифр',
        max_length=10)
    name = models.CharField(
        verbose_name='Название',
        max_length=100)
    specialization = models.CharField(
        verbose_name='Профиль (специализация)',
        max_length=200,
        blank=True)
    type = models.CharField(
        verbose_name='Квалификация',
        max_length=1,
        choices=SPECIALTY_TYPE_CHOICES,
        default='B')
    term = models.CharField(
        verbose_name='Термин',
        max_length=1,
        choices=SPECIALTY_TERM_CHOICES,
        default='D')
    standard_generation = models.CharField(
        verbose_name='Поколение стандарта',
        max_length=2,
        default='3',
        validators=[MinValueValidator('1'), MaxValueValidator('9')])
    max_level = models.IntegerField(
        verbose_name='Старший курс',
        default=4,
        validators=level_validator)
    chair = models.ForeignKey(Chair,
        verbose_name='Выпускающая кафедра',
        blank=True,
        null=True)

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

class Employee(Person):
    "Сотрудник"
    position = models.CharField(
        verbose_name='Должность',
        max_length=50,
        blank=True)
    degree = models.CharField(
        verbose_name='Учёная степень',
        max_length=20,
        blank=True)
    chair = models.ForeignKey(Chair,
        verbose_name='Кафедра',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'