from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.db.models import Max
from django.http import Http404

from .models import Course, CourseVersion


class CourseList(ListView):
    queryset = Course.objects\
        .select_related('specialty')\
        .filter(closed=False)\
        .all()

class CourseLastVersionDetail(TemplateView):
    template_name = 'courses/courseversion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseLastVersionDetail, self).get_context_data(**kwargs)

        max_version = CourseVersion.objects.filter(course=self.kwargs['pk'])\
            .aggregate(Max('version'))['version__max']
        try:
            context['courseversion'] = CourseVersion.objects\
                .get(version=max_version)
        except CourseVersion.DoesNotExist:
            context['courseversion'] = None

        try:
            context['course'] = Course.objects.\
                select_related('specialty', 'specialty__chair').\
                get(id=self.kwargs['pk'])
        except Course.DoesNotExist:
            raise Http404()
        return context