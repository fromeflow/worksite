from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courseworks.models import CourseWork
from diplomaworks.models import DiplomaWork
from students.models import Student, Group
from misc.form_mixins import SuperuserRequiredMixin


def index(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render_to_response('students/index.html', ctx,
                              context_instance=RequestContext(request))


def detail(request, student_id):
    try:
        student = Student.objects.select_related('group').get(id=student_id)
    except ObjectDoesNotExist:
        raise Http404
    courseworks = CourseWork.objects.filter(student=student)
    diplomaworks = DiplomaWork.objects.filter(student=student)
    return render_to_response('students/detail.html',
                              {
                                  'student': student,
                                  'courseworks': courseworks,
                                  'diplomaworks': diplomaworks,
                              },
                              context_instance=RequestContext(request))

class StudentCreate(SuperuserRequiredMixin, CreateView):
    model = Student
    # fields = ['name']


class StudentUpdate(SuperuserRequiredMixin, UpdateView):
    model = Student
    # fields = ['name']


class StudentDelete(SuperuserRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students-index')

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

