from os.path import join
from django.db import models
from django.core.urlresolvers import reverse

from students.models import Group


FINALEXAMS_FOLDER = 'finalexams'


# TODO Продумать схему переименования
def UPLOAD_TO(s, fn):
    return join(
        FINALEXAMS_FOLDER,
        str(s.group.graduation_year),
        fn)


class Finalexam(models.Model):
    title = models.CharField(verbose_name='Название экзамена',
                             max_length=100)
    date = models.DateTimeField(verbose_name='Дата проведения',
                                null=True, blank=True)
    group = models.ForeignKey(verbose_name='Группа',
                              to=Group)
    questions = models.FileField(verbose_name='Вопросы',
                                 upload_to=UPLOAD_TO,
                                 null=True, blank=True)

    def __str__(self):
        return '{year} - {spec}'.format(
            year=self.group.graduation_year,
            spec=self.group.speciality
        )

    def get_absolute_url(self):
        return reverse('finalexams-detail', kwargs={'finalexam_id': self.id})

    class Meta:
        ordering = ['-date', 'title']
        verbose_name = 'государственный экзамен'
        verbose_name_plural = 'государственные экзамены'