from os.path import join

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

SEMINARS_FOLDER = 'seminars'


class Seminar(models.Model):
    title = models.CharField(verbose_name='Тема',
                             max_length=100)
    speaker = models.CharField(verbose_name='Докладчик',
                               max_length=50, blank=True)
    speaker_user = models.ForeignKey(verbose_name='Связанный пользователь',
                                     to=User, blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата проведения',
                                blank=True, null=True)
    venue = models.CharField(verbose_name='Место проведения',
                             max_length=100,
                             blank=True, null=True)
    description = models.TextField(verbose_name='Описание семинара')

    def __str__(self):
        if self.date is None:
            return self.title
        return '{title} ({date})'.format(
            title=self.title,
            date=self.date.strftime('%d.%m.%Y')
        )

    def get_absolute_url(self):
        return reverse('seminars-detail', kwargs={'seminar_id': self.id})

    class Meta:
        ordering = ['-date']
        verbose_name = 'семинар'
        verbose_name_plural = 'семинары'


class SeminarMaterials(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=100)
    file = models.FileField(verbose_name='Материалы',
                            upload_to=lambda s, fn: join(SEMINARS_FOLDER, str(s.seminar.id), fn))
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    seminar = models.ForeignKey(verbose_name='Семинар',
                                to=Seminar)

    def __str__(self):
        return '{title} [{seminar}]'.format(
            title=self.title,
            seminar=self.seminar
        )

    class Meta:
        ordering = ['seminar']
        verbose_name = 'материал семинара'
        verbose_name_plural = 'материалы семинара'