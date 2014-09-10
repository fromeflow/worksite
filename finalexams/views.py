from django.views.generic.detail import DetailView

from django.views.generic.list import ListView

from finalexams.models import Finalexam


class FinalexamDetail(DetailView):
    model = Finalexam
    pk_url_kwarg = 'finalexam_id'


class FinalexamListView(ListView):
    model = Finalexam
