from django.db import models
from django.contrib.auth.models import User


SEX_CHOICES = (('M', 'М'), ('F', 'Ж'))

class Person(models.Model):
    "Человек"
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=30)
    name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        blank=True)
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=20,
        blank=True)
    sex = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=SEX_CHOICES)
    user = models.OneToOneField(User,
        verbose_name='Пользователь',
        blank=True,
        null=True)

    @property
    def surname_initials(self):
        "Фамилия с инициалами"
        s = self.surname.capitalize()
        if self.name: s += ' {n}.'.format(n=self.name[0].upper())
        if self.patronymic: s += ' {p}.'.format(p=self.patronymic[0].upper())
        return s

    def __str__(self):
        return self.surname_initials

    class Meta:
        ordering = ['surname']
        verbose_name = 'человек'
        verbose_name_plural = 'люди'