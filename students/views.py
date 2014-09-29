from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Count

from courseworks.models import CourseWork
from diplomaworks.models import DiplomaWork
from students.models import Student, Group
from misc.form_mixins import SuperuserRequiredMixin



# Студент =======================================
class StudentDetail(DetailView):
    model = Student
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        context['courseworks'] = CourseWork.objects.filter(student=self.object)
        context['diplomaworks'] = DiplomaWork.objects.filter(student=self.object)
        return context


class StudentCreate(SuperuserRequiredMixin, CreateView):
    model = Student


class StudentUpdate(SuperuserRequiredMixin, UpdateView):
    model = Student
    pk_url_kwarg = 'student_id'


class StudentDelete(SuperuserRequiredMixin, DeleteView):
    model = Student
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('students-group-index')


# Группа ========================================
class GroupListView(ListView):
    queryset = Group.objects.annotate(num_students=Count('student'))

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['students_total'] = Student.objects.count()
        return context


class GroupDetail(DetailView):
    queryset = Group.objects.select_related('speciality').all()
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['students'] = self.object.student_set.order_by('surname', 'name').all()
        return context
