from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from projects.models import CourseProject, FinalProject


# Списки
class CourseProjectList(ListView):
    queryset = CourseProject.objects\
        .select_related('student', 'student__group__specialty', 'course_semester__course_version')\
        .filter(~Q(student=None))\
        .order_by('course_semester', 'student__group')\
        .all()

class OpenProjectList(ListView):
    template_name_suffix = '_open_list'
    queryset = CourseProject.objects\
        .filter(student=None)\
        .all()

class FinalProjectList(ListView):
    queryset = FinalProject.objects\
        .select_related('student__group__specialty')\
        .all()

class OpenFinalProjectList(ListView):
    template_name_suffix = '_open_list'
    queryset = FinalProject.objects\
        .filter(student=None)\
        .all()

# Подробная информация
class CourseProjectDetail(DetailView):
    model = CourseProject

class FinalProjectDetail(DetailView):
    model = FinalProject