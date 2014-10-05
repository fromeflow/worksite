from django.db import models
from django.core.urlresolvers import reverse

from students.models import Student
from misc.utils import upload_student_work_to
from misc.validators import year_validator, mark5_validator
from misc.model_mixins import ToLinkMixin


DIPLOMAWORKS_FOLDER = 'diplomaworks'


def UPLOAD_TO(s, fn):
    return upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn)


def UPLOAD_TO_SLIDES(s, fn):
    return upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='слайды')


def UPLOAD_TO_MATERIALS(s, fn):
    return upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='материалы')


def UPLOAD_TO_REVIEW(s, fn):
    return upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='материалы')


def UPLOAD_TO_REVIEW_EXTERNAL(s, fn):
    return upload_student_work_to(s, DIPLOMAWORKS_FOLDER, fn, info='материалы')


class DiplomaWork(models.Model, ToLinkMixin):
    title = models.CharField(verbose_name='Тема', max_length=100)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    student = models.ForeignKey(verbose_name='Исполнитель', to=Student, default=None,
                                limit_choices_to={'sent_down': False},
                                blank=True, null=True)
    year = models.IntegerField(verbose_name='Учебный год',
                               blank=True, null=True,
                               validators=year_validator)
    mark = models.IntegerField(verbose_name='Оценка', default=None,
                               blank=True, null=True,
                               validators=mark5_validator)
    completed = models.BooleanField(verbose_name='Завершена', default=False)
    slides = models.FileField(verbose_name='Слайды',
                              upload_to=UPLOAD_TO_SLIDES,
                              blank=True, null=True)
    text = models.FileField(verbose_name='Текст',
                            upload_to=UPLOAD_TO,
                            blank=True, null=True)
    review = models.FileField(verbose_name='Отзыв руководителя',
                              upload_to=UPLOAD_TO_REVIEW,
                              blank=True, null=True)
    review_external = models.FileField(verbose_name='Внешняя рецензия',
                                       upload_to=UPLOAD_TO_REVIEW_EXTERNAL,
                                       blank=True, null=True)
    materials = models.FileField(verbose_name='Материалы',
                                 upload_to=UPLOAD_TO_MATERIALS,
                                 blank=True, null=True)


    def academic_year(self):
        if self.year is None:
            return None
        return '{year1}—{year2}'.format(
            year1=self.year,
            year2=self.year + 1
        )

    academic_year.short_description = 'Учебный год'

    link_icon_class = 'glyphicon glyphicon-file'

    def link_str(self):
        return '«' + self.title + '»'

    def __str__(self):
        s = self.title
        if self.student is not None:
            s += ' ({student})'.format(
                student=self.student.surname_initials
            )
        return s

    def get_absolute_url(self):
        return reverse('diplomaworks-detail', kwargs={'diplomawork_id': self.id})

    class Meta:
        ordering = ['-year', 'student__surname']
        verbose_name = 'квалификационная работа'
        verbose_name_plural = 'квалификационные работы'
