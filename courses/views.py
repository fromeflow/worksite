from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError

from braces.views import StaffuserRequiredMixin

from .models import Course, CourseVersion
from .form import CourseForm, CourseVersionForm


class CourseList(ListView):
    queryset = Course.objects\
        .select_related('specialty')\
        .all()

class CourseLastVersionRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        course_id = self.kwargs['pk']
        courseversion = get_object_or_404(Course, pk=course_id).actual_version
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
        context = super().get_context_data(**kwargs)
        context['course'] = context['courseversion'].course
        context['groups'] = context['course'].version_groups
        context['semesters'] = context['courseversion'].coursesemester_set.all()
        return context


class CourseUpdate(StaffuserRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm


class CourseDelete(StaffuserRequiredMixin, DeleteView):
    template_name = '_gen/confirm_delete.html'
    model = Course
    success_url = reverse_lazy('courses:index')


class CourseCreate(StaffuserRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm


class CourseVersionUpdate(StaffuserRequiredMixin, UpdateView):
    model = CourseVersion
    form_class = CourseVersionForm


class CourseVersionDelete(StaffuserRequiredMixin, DeleteView):
    template_name = '_gen/confirm_delete.html'
    model = CourseVersion
    def get_success_url(self):
        return reverse_lazy('courses:course-last-version-redirect', kwargs={'pk': self.object.course_id})


class CourseVersionCreate(StaffuserRequiredMixin, CreateView):
    model = CourseVersion
    form_class = CourseVersionForm

    def form_valid(self, form):
        course = get_object_or_404(Course, id=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.course = course
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('group', 'Курс не может повторяться у группы')
            return self.form_invalid(form)
