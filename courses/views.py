from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

        versions = CourseVersion.objects.filter(course=self.kwargs['pk']).\
            values('id', 'version')
        try:
            max_version_id = max(versions, key=lambda x: x['version'])['id']
            context['courseversion'] = CourseVersion.objects.get(id=max_version_id)
        except ValueError:
            pass

        try:
            context['course'] = Course.objects.\
                select_related('specialty', 'specialty__chair').\
                get(id=self.kwargs['pk'])
        except Course.DoesNotExist:
            raise Http404()
        return context

class CourseVersionDetail(DetailView):
    queryset = CourseVersion.objects.\
        select_related('course', 'course__specialty').\
        all()

    def get_context_data(self, **kwargs):
        context = super(CourseVersionDetail, self).get_context_data(**kwargs)
        context['course'] = context['courseversion'].course
        return context