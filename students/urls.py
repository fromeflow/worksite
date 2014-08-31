from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'students.views.index'),
                       url(r'^(?P<student_id>\d+)$', 'students.views.detail'),
                       url(r'^(?P<student_id>\d+)-edit$', 'students.views.edit'),
                       url(r'^group-(?P<group_id>\d+)$', 'students.views.group_detail'),
)

