from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

from seminars.models import Seminar, SeminarMaterials
from misc.form_mixins import SuperuserRequiredMixin


# Семинар =======================================
class SeminarListView(ListView):
    model = Seminar


class SeminarDetail(DetailView):
    model = Seminar
    pk_url_kwarg = 'seminar_id'

    def get_context_data(self, **kwargs):
        context = super(SeminarDetail, self).get_context_data(**kwargs)
        context['materials'] = SeminarMaterials.objects.filter(seminar=self.object)
        return context


# Материалы семинара ============================
class SeminarMaterialsCreate(SuperuserRequiredMixin, CreateView):
    model = SeminarMaterials
    fields = ['title', 'description', 'file']

    def get_context_data(self, **kwargs):
        context = super(SeminarMaterialsCreate, self).get_context_data(**kwargs)
        context['seminar'] = get_object_or_404(Seminar, id=self.kwargs['seminar_id'])
        return context

    def form_valid(self, form):
        self.success_url = reverse_lazy('seminars-detail',
                                        kwargs={'seminar_id': self.kwargs['seminar_id']})
        form.instance.seminar = get_object_or_404(Seminar, id=self.kwargs['seminar_id'])
        return super(SeminarMaterialsCreate, self).form_valid(form)