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
        context['materials'] = context['textbook'].textbookfile_set.all()
        context['materials_count'] = context['textbook'].textbookfile_set.count()
        return context