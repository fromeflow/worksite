from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from braces.views import StaffuserRequiredMixin, LoginRequiredMixin

from students.models import Group, Student
from projects.models import CourseProject, FinalProject

# Группа ========================================
class GroupList(ListView):
    queryset = Group.objects\
        .select_related('specialty')\
        .annotate(num_students=Count('student'))\
        .all()

    def get_context_data(self, **kwargs):
        context = super(GroupList, self).get_context_data(**kwargs)
        context['students_total'] = Student.objects.count()
        return context


class GroupDetail(LoginRequiredMixin, DetailView):
    queryset = Group.objects.select_related('specialty')\
        .all()

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['students'] = self.object.student_set.order_by('surname', 'name').all()
        return context


class GroupCreate(StaffuserRequiredMixin, CreateView):
    model = Group
    fields = '__all__'

class GroupUpdate(StaffuserRequiredMixin, UpdateView):
    model = Group
    fields = '__all__'


class GroupDelete(StaffuserRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('students:group-index')


# Студент =======================================
class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        context['course_projects'] = CourseProject.objects.filter(student=self.object)
        context['final_projects'] = FinalProject.objects.filter(student=self.object)
        return context


class StudentCreate(StaffuserRequiredMixin, CreateView):
    model = Student
    fields = '__all__'

class GroupAddStudent(StaffuserRequiredMixin, CreateView):
    model = Student
    fields = ['surname', 'name', 'patronymic', 'sex', 'sent_down', 'user']

    def get_context_data(self, **kwargs):
        context = super(GroupAddStudent, self).get_context_data(**kwargs)
        context['group'] = get_object_or_404(Group, id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self.success_url = reverse_lazy('students:group-detail',
                                        kwargs={'pk': self.kwargs['pk']})
        form.instance.group = get_object_or_404(Group, id=self.kwargs['pk'])
        return super(GroupAddStudent, self).form_valid(form)


class StudentUpdate(StaffuserRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'

class StudentDelete(StaffuserRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:group-index')