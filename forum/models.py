from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    title = models.CharField(verbose_name='Тема',
                             max_length=50)
    creation_date = models.DateTimeField(verbose_name='Дата создания',
                                         default=datetime.now)
    creator = models.ForeignKey(verbose_name='Создатель',
                                to=User)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'тема'
        verbose_name_plural = 'темы'


class Message(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    post_date = models.DateTimeField(verbose_name='Дата публикации',
                                     default=datetime.now)
    creator = models.ForeignKey(verbose_name='Автор',
                                to=User)
    theme = models.ForeignKey(verbose_name='Связанная тема',
                              to=Theme)

    def __str__(self):
        return str(self.text)[:20]

    class Meta:
        ordering = ['theme', '-post_date']
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'