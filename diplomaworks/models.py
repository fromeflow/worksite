from django.db import models
from django.core.urlresolvers import reverse

import diplomaworks
from students.models import Student
from misc.utils import upload_student_work_to
from misc.validators import work_year_validator, mark5_validator


DIPLOMAWORKS_FOLDER = 'diplomaworks'

class DiplomaWork(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=100)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    student = models.ForeignKey(verbose_name='Исполнитель', to=Student, default=None,
                                limit_choices_to={'sent_down': False},
                                blank=True, null=True)
    year = models.IntegerField(verbose_name='Учебный год',
                               blank=True, null=True,
                               validators=work_year_validator)
    mark = models.IntegerField(verbose_name='Оценка', default=None,
                               blank=True, null=True,
                               validators=mark5_validator)
    completed = models.BooleanField(verbose_name='Завершена', default=False)
    slides = models.FileField(verbose_name='Слайды',
                              upload_to=lambda s, fn: upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='слайды'),
                              blank=True, null=True)
    text = models.FileField(verbose_name='Текст',
                            upload_to=lambda s, fn: upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn),
                            blank=True, null=True)
    review = models.FileField(verbose_name='Отзыв руководителя',
                            upload_to=lambda s, fn: upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='отзыв'),
                            blank=True, null=True)
    review_external = models.FileField(verbose_name='Внешняя рецензия',
                            upload_to=lambda s, fn: upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='рецензия'),
                            blank=True, null=True)
    materials = models.FileField(verbose_name='Материалы',
                                 upload_to=lambda s, fn: upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='материалы'),
                                 blank=True, null=True)


    def academic_year(self):
        if self.year is None:
            return None
        return '{year1}—{year2}'.format(
            year1=self.year,
            year2=self.year + 1
        )
    academic_year.short_description = 'Учебный год'

    def to_link(self):
        return '<span class="{cls}"></span>&nbsp;<a href="{link}">{text}</a>' \
            .format(
            link=reverse(diplomaworks.views.detail, kwargs={'diplomawork_id': self.id}),
            text='«' + self.title + '»',
            cls='text-muted glyphicon glyphicon-file'
        )

    def __str__(self):
        s = self.title
        if self.student is not None:
            s += ' ({student})'.format(
                student=self.student.surname_initials
            )
        return s

    class Meta:
        ordering = ['-year', 'student__surname']
        verbose_name = 'квалификационная работа'
        verbose_name_plural = 'квалификационные работы'
