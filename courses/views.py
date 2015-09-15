from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Max

from .models import Course, CourseVersion


class CourseList(ListView):
    queryset = Course.objects\
        .select_related('specialty')\
        .filter(closed=False)\
        .all()

class CourseLastVersionDetail(DetailView):
    template_name = 'courses/courseversion_detail.html'
    def get_object(self):
        max_version = CourseVersion.objects.filter(id=self.kwargs['pk'])\
            .aggregate(Max('version'))['version__max']
        try:
            last_course_version = CourseVersion.objects\
                .get(version=max_version)
        except CourseVersion.DoesNotExist:
            return None
        return last_course_version
