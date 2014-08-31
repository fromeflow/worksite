from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext

from courseworks.models import CourseWork
from diplomaworks.models import DiplomaWork
from students.models import Student, Group
from students.forms import StudentForm
import students


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


# FIXME: check permissions
def edit(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(students.views.detail, kwargs={'student_id': student_id}))
    else:
        form = StudentForm(instance=student)
    ctx = {
        'student': student,
        'form': form
    }
    ctx.update(csrf(request))
    return render_to_response('students/edit.html', ctx,
                              context_instance=RequestContext(request))


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

