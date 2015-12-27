from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Textbook


class TextbookList(ListView):
    model = Textbook


class TextbookDetail(DetailView):
    model = Textbook