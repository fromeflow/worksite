from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Textbook


class TextbookList(ListView):
    model = Textbook


class TextbookDetail(DetailView):
    model = Textbook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        textbook = context['textbook']
        context['materials'] = textbook.textbookfile_set.all()
        context['materials_count'] = textbook.textbookfile_set.count()
        context['courses'] = textbook.courses.all()
        return context