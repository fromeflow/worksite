from os.path import join
from django.db import models
from django.core.urlresolvers import reverse

from courses.models import Course
from misc.validators import year_validator


TEXTBOOKS_FOLDER = 'textbooks'


def UPLOAD_TO(s, fn):
    return join(TEXTBOOKS_FOLDER, str(s.textbook.title), fn)


# TODO Добавить вывод полной информации о книге
class Textbook(models.Model):
    authors = models.CharField(verbose_name='Авторы',
                               max_length=200,
                               default='Великодный В. И.')
    compiler = models.BooleanField(verbose_name='Составитель',
                                   default=False)
    title = models.CharField(verbose_name='Название',
                             max_length=200)
    publisher = models.CharField(verbose_name='Издательство',
                                 max_length=100,
                                 blank=True, null=True)
    year = models.IntegerField(verbose_name='Год издания',
                               validators=[year_validator],
                               blank=True, null=True)
    course = models.ManyToManyField(verbose_name='Дисциплина',
                                    to=Course,
                                    blank=True, null=True)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('textbooks-detail', kwargs={'textbook_id': self.id})

    class Meta:
        ordering = ['title']
        verbose_name = 'пособие'
        verbose_name_plural = 'пособия'
        unique_together = (('title',),)


# TODO Проверить работу order_with_respect_to
class TextbookMaterial(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=100)
    file = models.FileField(verbose_name='Материалы',
                            upload_to=UPLOAD_TO)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    textbook = models.ForeignKey(verbose_name='Пособие',
                                 to=Textbook)

    def __str__(self):
        return '{title} [{seminar}]'.format(
            title=self.title,
            seminar=self.seminar
        )

    class Meta:
        ordering = ['title']
        verbose_name = 'материал пособия'
        verbose_name_plural = 'материалы пособия'
        order_with_respect_to = 'textbook'