from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.template import RequestContext

from courseworks.models import CourseWork


def index(request):
    qs_current = CourseWork.objects.select_related('student', 'course', 'course__speciality').filter(
        student__isnull=False, completed=False).order_by('-year')
    return render_to_response('courseworks/index.html',
                              {
                                  'works_current': qs_current
                              },
                              context_instance=RequestContext(request))


def finished(request):
    qs_finished = CourseWork.objects \
        .select_related('student', 'course', 'course__speciality') \
        .filter(student__isnull=False, completed=True) \
        .order_by('-year')
    return render_to_response('courseworks/finished.html',
                              {
                                  'works_finished': qs_finished,
                              },
                              context_instance=RequestContext(request))


def open(request):
    qs_wo_student = CourseWork.objects \
        .select_related('student', 'course', 'course__speciality') \
        .filter(student__isnull=True) \
        .order_by('-course', 'title')
    return render_to_response('courseworks/open.html',
                              {
                                  'works_wo_student': qs_wo_student,
                              },
                              context_instance=RequestContext(request))


def detail(request, coursework_id):
    try:
        work = CourseWork.objects.select_related('student', 'course').get(id=coursework_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('courseworks/details.html', {'work': work},
                              context_instance=RequestContext(request))
