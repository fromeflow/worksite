from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.db.models import Max
from django.core.urlresolvers import reverse_lazy

from .models import Course, CourseVersion


class CourseList(ListView):
    queryset = Course.objects\
        .select_related('specialty')\
        .filter(closed=False)\
        .all()

class CourseLastVersionRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        course_id = self.kwargs['pk']
        max_version = CourseVersion.objects.filter(course=course_id)\
            .aggregate(Max('version'))['version__max']
        try:
            courseversion = CourseVersion.objects.filter(course=course_id)\
                .get(version=max_version)
        except CourseVersion.DoesNotExist:
            return reverse_lazy('courses:course-detail', kwargs={'pk': course_id})
        return reverse_lazy('courses:course-version-detail', kwargs={'pk': courseversion.id})

class CourseDetail(DetailView):
    template_name = 'courses/courseversion_detail.html'
    model = Course

class CourseVersionDetail(DetailView):
    queryset = CourseVersion.objects.\
        select_related('course', 'course__specialty').\
        all()

    def get_context_data(self, **kwargs):
        context = super(CourseVersionDetail, self).get_context_data(**kwargs)
        context['course'] = context['courseversion'].course
        return context