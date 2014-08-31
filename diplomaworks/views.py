from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.template import RequestContext

from diplomaworks.models import DiplomaWork


def index(request):
    works_current = DiplomaWork.objects.select_related('student', 'student__group').filter(
        student__isnull=False, completed=False).order_by('-year')
    works_finished = DiplomaWork.objects.select_related('student', 'student__group').filter(
        student__isnull=False, completed=True).order_by('-year')
    return render_to_response('diplomaworks/index.html',
                              {
                                  'works_current': works_current,
                                  'works_finished': works_finished,
                              },
                              context_instance=RequestContext(request))

def open(request):
    qs_wo_student = DiplomaWork.objects \
        .select_related('student') \
        .filter(student__isnull=True) \
        .order_by('title')
    return render_to_response('courseworks/open.html',
                              {
                                  'works_wo_student': qs_wo_student,
                              },
                              context_instance=RequestContext(request))


def detail(request, diplomawork_id):
    try:
        work = DiplomaWork.objects.select_related('student').get(id=diplomawork_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('diplomaworks/details.html', {'work': work},
                              context_instance=RequestContext(request))