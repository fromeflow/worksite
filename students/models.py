from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse_lazy

from university.models import Specialty, Employee
from accounts.models import Person

from utils.validators import year_validators
from utils.mixins import ToLinkMixin

class Group(ToLinkMixin, models.Model):
    "Академическая группа"
    suffix = models.CharField(verbose_name='Суффикс специальности', max_length=2)
    specialty = models.ForeignKey(to=Specialty, verbose_name='Специальность')
    entrance_year = models.IntegerField(verbose_name='Год поступления', validators=year_validators)
    code = models.CharField(verbose_name='Шифр', max_length=10, blank=True)
    distance_learning = models.BooleanField(verbose_name='Заочное обучение', default=False)
    supervisor = models.ForeignKey(to=Employee, verbose_name='Куратор', null=True, blank=True, default=None)

    @property
    def level(self):
        diff = datetime.now().year - self.entrance_year
        month = datetime.now().month
        return diff if month <= 8 else diff + 1

    @property
    def semester(self):
        diff = datetime.now().year - self.entrance_year
        month = datetime.now().month
        return diff if month > 8 else diff * 2 + 1

    @property
    def name(self):
        return '{level}{suffix}'.format(
            level=min(self.level, self.specialty.max_level),
            suffix=self.suffix)

    @property
    def full_name(self):
        return str(self)

    @property
    def years(self):
        return "{begin}—{end}".format(
            begin=self.entrance_year,
            end=self.graduation_year
        )

    @property
    def graduation_year(self):
        return self.entrance_year + self.specialty.max_level

    @property
    def finished(self):
        return self.level > self.specialty.max_level

    def semester_to_year(self, semester):
        return (semester - 1) // 2 + self.entrance_year

    def __str__(self):
        name = self.name
        if self.level > self.specialty.max_level:
            name += ' (’{year})'.format(
                name=self.name,
                year=self.entrance_year + self.specialty.max_level
            )
        return name

    def get_absolute_url(self):
        return reverse_lazy('students:group-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-entrance_year', 'suffix']
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        unique_together = (('suffix', 'entrance_year'),)


class Student(ToLinkMixin, Person):
    "Студент"
    group = models.ForeignKey(to=Group, verbose_name="Группа")
    sent_down = models.BooleanField(verbose_name='Отчислен', default=False)

    def __str__(self):
        s = self.surname_initials
        s += ' [{group}]'.format(group=self.group)
        return s

    def get_absolute_url(self):
        return reverse_lazy('students:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['group', 'surname']
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def link_str(self):
        if self.sent_down:
            return self.surname_initials
        return self.surname_initials