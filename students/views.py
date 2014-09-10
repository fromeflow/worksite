from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from courseworks.models import CourseWork
from diplomaworks.models import DiplomaWork
from students.models import Student, Group
from misc.form_mixins import SuperuserRequiredMixin


# Студент =======================================
class StudentDetail(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        context['courseworks'] = CourseWork.objects.filter(student=self.object)
        context['diplomaworks'] = DiplomaWork.objects.filter(student=self.object)
        return context


class StudentCreate(SuperuserRequiredMixin, CreateView):
    model = Student


class StudentUpdate(SuperuserRequiredMixin, UpdateView):
    model = Student


class StudentDelete(SuperuserRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students-group-index')


# Группа ========================================
class GroupListView(ListView):
    model = Group


def group_detail(request, group_id):
    try:
        group = Group.objects.select_related('speciality').get(id=group_id)
    except ObjectDoesNotExist:
        raise Http404
    students = group.student_set.order_by('surname', 'name').all()
    return render_to_response('students/group_detail.html',
                              {
                                  'group': group,
                                  'students': students
                              },
                              context_instance=RequestContext(request))

