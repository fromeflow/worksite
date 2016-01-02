from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from braces.views import StaffuserRequiredMixin

from .models import Textbook, TextbookFile
from .form import TextbookForm, TextbookFileForm

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

# TextbookFile views

class TextbookFileCreate(StaffuserRequiredMixin, CreateView):
    model = TextbookFile
    form_class = TextbookFileForm

    def form_valid(self, form):
        textbook = get_object_or_404(Textbook, id=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.textbook = textbook
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('textbooks:detail', kwargs={'pk': self.kwargs['pk']})

class TextbookFileUpdate(StaffuserRequiredMixin, UpdateView):
    model = TextbookFile
    form_class = TextbookFileForm

    def get_success_url(self):
        textbook = textbook = get_object_or_404(TextbookFile, id=self.kwargs['pk']).textbook
        return reverse_lazy('textbooks:detail', kwargs={'pk': textbook.id})

class TextbookFileDelete(StaffuserRequiredMixin, DeleteView):
    template_name = '_gen/confirm_delete.html'
    model = TextbookFile

    def get_success_url(self):
        textbook = textbook = get_object_or_404(TextbookFile, id=self.kwargs['pk']).textbook
        return reverse_lazy('textbooks:detail', kwargs={'pk': textbook.id})