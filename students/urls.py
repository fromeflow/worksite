from django.conf.urls import patterns, url

from students.views import \
    StudentUpdate, StudentCreate, StudentDelete, StudentDetail, \
    GroupListView, GroupDetail, GroupCreate, GroupUpdate, GroupDelete

urlpatterns = \
    patterns('',
             url(r'^$', GroupListView.as_view(), name='students-group-index'),
             url(r'^group-(?P<group_id>\d+)$', GroupDetail.as_view(), name='students-group-detail'),
             url(r'^group-create$', GroupCreate.as_view(), name='students-group-create'),
             url(r'^group-(?P<group_id>\d+)-edit$', GroupUpdate.as_view(), name='students-group-edit'),
             url(r'^group-(?P<group_id>\d+)-delete$', GroupDelete.as_view(), name='students-group-delete'),

             url(r'^(?P<student_id>\d+)$', StudentDetail.as_view(), name='students-detail'),
             url(r'^(?P<student_id>\d+)-edit$', StudentUpdate.as_view(), name='students-edit'),
             url(r'^create$', StudentCreate.as_view(), name='students-create'),
             url(r'^(?P<student_id>\d+)-delete$', StudentDelete.as_view(), name='students-delete'),
    )
