from os.path import splitext, join

from django.db import models
from django.core.urlresolvers import reverse

from students.models import Student
from university.models import Employee
from courses.models import CourseSemester

from utils.validators import mark5_validator, year_validator
from utils.mixins import ToLinkMixin
from utils.private_storage.storage import private_storage


PROJECTS_FOLDER = 'projects'

def upload_project_to(self, filename, info=None):
    if info is None:
        info = ''
    else:
        info = ' (' + info + ')'
    id = str(self.id)
    if self.student:
        name = str(self.student.surname) + ' - '
    else:
        name = ''
    title = str(self.title)
    ext = splitext(filename)[1].lower()
    fullname = '{name}{title}{info}{ext}'.format(
        name=name,
        title=title,
        info=info,
        ext=ext
    )
    return join(PROJECTS_FOLDER, id, fullname)


def UPLOAD_PROJECT_TEXT(s, fn): return upload_project_to(s, fn)
def UPLOAD_PROJECT_SLIDES(s, fn): return upload_project_to(s, fn, 'слайды')
def UPLOAD_PROJECT_MATERIALS(s, fn): return upload_project_to(s, fn, 'материалы')

class GenericProject(models.Model):
    "Студенческий проект"
    title = models.CharField(verbose_name='Тема', max_length=100)
    description = models.TextField(verbose_name='Описание', blank=True)
    student = models.ForeignKey(to=Student, verbose_name='Исполнитель', blank=True, null=True, default=None,
                                limit_choices_to={'sent_down': False})
    supervisor = models.ForeignKey(to=Employee, verbose_name='Руководитель', blank=True, null=True, default=None)
    mark = models.IntegerField(verbose_name='Оценка', blank=True, null=True, default=None, validators=mark5_validator)
    completed = models.BooleanField(verbose_name='Завершена', default=False)
    text = models.FileField(verbose_name='Текст', blank=True, null=True,
                            max_length=150, storage=private_storage,
                            upload_to=UPLOAD_PROJECT_TEXT)
    slides = models.FileField(verbose_name='Слайды', blank=True, null=True,
                              max_length=150, storage=private_storage,
                              upload_to=UPLOAD_PROJECT_SLIDES)
    materials = models.FileField(verbose_name='Материалы', blank=True, null=True,
                                 max_length=150, storage=private_storage,
                                 upload_to=UPLOAD_PROJECT_MATERIALS)

    def __str__(self):
        s = '«' + self.title + '»'
        if self.student is not None:
            s += ' ({student})'.format(
                student=self.student.surname_initials
            )
        return s

    class Meta:
        ordering = ['title']
        verbose_name = 'студенческая работа'
        verbose_name_plural = 'студенческие работы'

class CourseProject(ToLinkMixin, GenericProject):
    "Курсовая работа"
    course_semester = models.ForeignKey(to=CourseSemester, verbose_name='Семестр курса',
                                        blank=True, null=True, default=None)

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-course_semester__course_version', '-course_semester', 'student__surname']
        verbose_name = 'курсовая работа'
        verbose_name_plural = 'курсовые работы'

    def link_str(self):
        return '«' + self.title + '»'

class FinalProject(ToLinkMixin, GenericProject):
    "Квалификационная работа"

    def defence_year(self):
        try:
            return self.student.group.graduation_year
        except AttributeError:
            return None

    defence_year.short_description = 'Учебный год'

    def get_absolute_url(self):
        return reverse('projects:final-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['student__group', 'student__surname', 'title']
        verbose_name = 'квалификационная работа'
        verbose_name_plural = 'квалификационные работы'

    def link_str(self):
        return '«' + self.title + '»'

