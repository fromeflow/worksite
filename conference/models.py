from os.path import join
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse

from students.models import Student
from courses.models import Chair
from misc.validators import year_validator
from misc.model_mixins import ToLinkMixin


CONFERENCE_FOLDER = 'conference'


def UPLOAD_TO(s, fn):
    return join(CONFERENCE_FOLDER, str(s.report.id), fn)


class Report(models.Model, ToLinkMixin):
    title = models.CharField(verbose_name='Тема',
                             max_length=100)
    student = models.ForeignKey(verbose_name='Студент',
                                to=Student)
    description = models.TextField(verbose_name='Описание работы',
                                   blank=True)
    chair = models.ForeignKey(verbose_name='Кафедра',
                              to=Chair,
                              null=True)
    place = models.IntegerField(verbose_name='Место',
                                validators=[MinValueValidator(1), MaxValueValidator(3)],
                                blank=True, null=True)
    year = models.IntegerField(verbose_name='Учебный год',
                               validators=year_validator)

    def __str__(self):
        return '{student} «{title}»'.format(
            student=self.student.surname_initials,
            title=self.title
        )

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'report_id': self.id})

    class Meta:
        ordering = ['-year', 'title']
        verbose_name = 'доклад'
        verbose_name_plural = 'доклады'


class ReportFile(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=100)
    file = models.FileField(verbose_name='Материалы',
                            upload_to=UPLOAD_TO)
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    report = models.ForeignKey(verbose_name='Доклад',
                               to=Report)

    def __str__(self):
        return '{title} [{report}]'.format(
            title=self.title,
            report=self.report
        )

    class Meta:
        ordering = ['report']
        verbose_name = 'материал доклада'
        verbose_name_plural = 'материалы доклада'