from django.conf.urls import patterns, url

from students.views import StudentUpdate, StudentCreate, StudentDelete, StudentDetail, GroupListView, GroupDetail

urlpatterns = \
    patterns('',
             url(r'^$', GroupListView.as_view(), name='students-group-index'),
             url(r'^group-(?P<group_id>\d+)$', GroupDetail.as_view(), name='students-group-detail'),

             url(r'^(?P<pk>\d+)$', StudentDetail.as_view(), name='students-detail'),
             url(r'^(?P<pk>\d+)-edit$', StudentUpdate.as_view(), name='students-edit'),
             url(r'^create$', StudentCreate.as_view(), name='students-create'),
             url(r'^(?P<pk>\d+)-delete$', StudentDelete.as_view(), name='students-delete'),
    )
