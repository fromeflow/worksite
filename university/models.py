from django.db import models
from account.models import Person

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
        return self.name

    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'


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