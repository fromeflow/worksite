from django.conf.urls import patterns, url

from students.views import StudentUpdate, StudentCreate, StudentDelete

urlpatterns = patterns('',
                       url(r'^$', 'students.views.index',
                           name='students-index'),
                       url(r'^(?P<student_id>\d+)$', 'students.views.detail',
                           name='students-detail'),
                       url(r'^(?P<pk>\d+)-edit$', StudentUpdate.as_view(),
                           name='students-edit'),
                       url(r'create', StudentCreate.as_view(),
                           name='students-create'),
                       url(r'^(?P<pk>\d+)-delete$', StudentDelete.as_view(),
                           name='students-delete'),
                       url(r'^group-(?P<group_id>\d+)$', 'students.views.group_detail',
                           name='students-group-detail'),
)
