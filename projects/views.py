from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import CourseProject, FinalProject

class CourseProjectDetail(DetailView):
    model = CourseProject

class FinalProjectDetail(DetailView):
    model = FinalProject