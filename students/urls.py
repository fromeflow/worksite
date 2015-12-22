from django.conf.urls import patterns, url

from students.views import *


urlpatterns = [
     url(r'^$', GroupList.as_view(), name='group-index'),
     url(r'^group-(?P<pk>\d+)$', GroupDetail.as_view(), name='group-detail'),
     url(r'^group-create$', GroupCreate.as_view(), name='group-create'),
     url(r'^group-(?P<pk>\d+)-edit$', GroupUpdate.as_view(), name='group-edit'),
     url(r'^group-(?P<pk>\d+)-delete$', GroupDelete.as_view(), name='group-delete'),
     url(r'^group-(?P<pk>\d+)-add-student$', GroupAddStudent.as_view(), name='group-add-student'),
     url(r'^(?P<pk>\d+)$', StudentDetail.as_view(), name='detail'),
     url(r'^(?P<pk>\d+)-edit$', StudentUpdate.as_view(), name='edit'),
     url(r'^create$', StudentCreate.as_view(), name='create'),
     url(r'^(?P<pk>\d+)-delete$', StudentDelete.as_view(), name='delete'),
]
