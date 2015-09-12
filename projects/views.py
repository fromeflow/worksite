from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import CourseProject, FinalProject


# Списки
class CourseProjectList(ListView):
    queryset = CourseProject.objects\
        .select_related('student')\
        .all()

class OpenProjectList(ListView):
    template_name_suffix = '_open_list'
    queryset = CourseProject.objects\
        .filter(student=None)\
        .all()

class FinalProjectList(ListView):
    queryset = FinalProject.objects\
        .select_related('student')\
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