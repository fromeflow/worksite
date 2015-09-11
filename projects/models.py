from os.path import splitext, join

from django.db import models
from django.core.urlresolvers import reverse

from students.models import Student
from university.models import Employee
from utils.validators import mark5_validator, year_validator
from utils.mixins import ToLinkMixin


PROJECTS_FOLDER = 'projects'

def upload_project_to(self, filename, info=None):
    if info is None:
        info = ''
    else:
        info = ' (' + info + ')'
    id = str(self.id)
    if self.student:
        name = str(self.student.surname_initials) + ' - '
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
                            upload_to=UPLOAD_PROJECT_TEXT)
    slides = models.FileField(verbose_name='Слайды', blank=True, null=True,
                              upload_to=UPLOAD_PROJECT_SLIDES)
    materials = models.FileField(verbose_name='Материалы', blank=True, null=True,
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
    year = models.IntegerField(verbose_name='Учебный год', blank=True, null=True, validators=year_validator)
    semester = models.CharField(verbose_name='Семестр', max_length=1, blank=True, null=True,
                                choices=(('1', 1), ('2', 2)))
    # course_semester = ссылка на семестр дисциплины, после добавления убрать year, semester

    def academic_year(self):
        if self.year is None:
            return None
        return '{year1}—{year2}'.format(
            year1=self.year,
            year2=self.year + 1
        )

    academic_year.short_description = 'Учебный год'

    def get_absolute_url(self):
        return reverse('courseworks-detail', kwargs={'coursework_id': self.id})

    class Meta:
        ordering = ['-year', 'student__surname']
        verbose_name = 'курсовая работа'
        verbose_name_plural = 'курсовые работы'

    def link_icon_str(self):
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
        return reverse('diplomaworks-detail', kwargs={'diplomawork_id': self.id})

    class Meta:
        ordering = ['student__group', 'student__surname']
        verbose_name = 'квалификационная работа'
        verbose_name_plural = 'квалификационные работы'

    def link_icon_str(self):
        return '«' + self.title + '»'

