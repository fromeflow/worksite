from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'students.views.index',
                           name='students-index'),
                       url(r'^(?P<student_id>\d+)$', 'students.views.detail',
                           name='students-detail'),
                       url(r'^(?P<student_id>\d+)-edit$', 'students.views.edit',
                           name='students-edit'),
                       url(r'^group-(?P<group_id>\d+)$', 'students.views.group_detail',
                           name='students-group-detail'),
)

