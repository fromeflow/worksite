from os.path import join
from django.db import models
from django.core.urlresolvers import reverse
from utils.validators import year_validators
from courses.models import Course

TEXTBOOKS_FOLDER = 'textbooks'

def upload_textbook_files_to(self, filename):
    return join(TEXTBOOKS_FOLDER, self.textbook.title, filename)


class Textbook(models.Model):
    authors = models.CharField(verbose_name='Авторы', max_length=200)
    is_compiler = models.BooleanField(verbose_name='Составитель?', default=False)
    title = models.CharField(verbose_name='Название', max_length=200)
    publisher = models.CharField(verbose_name='Издательство', max_length=100, blank=True)
    year = models.IntegerField(verbose_name='Год издания', validators=year_validators, blank=True, null=True)
    courses = models.ManyToManyField(verbose_name='Курсы', to=Course, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return '{} «{}»'.format(self.authors, self.title)

    def get_absolute_url(self):
        return reverse('textbooks:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['title']
        verbose_name = 'пособие'
        verbose_name_plural = 'пособия'
        unique_together = ('title',)


class TextbookFile(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    file = models.FileField(verbose_name='Файл', upload_to=upload_textbook_files_to)
    description = models.TextField(verbose_name='Описание', blank=True)
    textbook = models.ForeignKey(verbose_name='Пособие', to=Textbook)

    def __str__(self):
        return '{}: {}'.format(self.textbook, self.title)

    class Meta:
        ordering = ['textbook', 'title']
        verbose_name = 'материалы пособия'
        verbose_name_plural = 'материалы пособия'
        unique_together = ('textbook', 'title')
