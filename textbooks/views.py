from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import StaffuserRequiredMixin

from .models import Textbook
from .form import TextbookForm

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


class TextbookUpdate(StaffuserRequiredMixin, UpdateView):
    model = Textbook
    form_class = TextbookForm


class TextbookDelete(StaffuserRequiredMixin, DeleteView):
    template_name = '_gen/confirm_delete.html'
    model = Textbook
    success_url = reverse_lazy('textbooks:index')


class TextbookCreate(StaffuserRequiredMixin, CreateView):
    model = Textbook
    form_class = TextbookForm