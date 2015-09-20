from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max

from .models import Course, CourseVersion


class CourseList(ListView):
    queryset = Course.objects\
        .select_related('specialty')\
        .annotate(last_version_a=Max('courseversion'))\
        .all()

class CourseLastVersionRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        course_id = self.kwargs['pk']
        courseversion = get_object_or_404(Course, pk=course_id).last_version
        if courseversion is None:
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
        context['versions'] = context['course'].version_numbers
        context['semesters'] = context['courseversion'].coursesemester_set.all()
        return context