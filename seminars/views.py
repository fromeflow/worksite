from django.views.generic.detail import DetailView

from seminars.models import Seminar, SeminarMaterials

# Семинар =======================================
class SeminarDetail(DetailView):
    model = Seminar
    pk_url_kwarg = 'seminar_id'

    def get_context_data(self, **kwargs):
        context = super(SeminarDetail, self).get_context_data(**kwargs)
        context['materials'] = SeminarMaterials.objects.filter(seminar=self.object)
        return context
