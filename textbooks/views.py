from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from textbooks.models import Textbook


class TextbookListView(ListView):
    model = Textbook


class TextbookDetail(DetailView):
    model = Textbook
    pk_url_kwarg = 'textbook_id'
