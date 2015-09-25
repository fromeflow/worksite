from django.conf.urls import patterns, url

from .views import *


urlpatterns = \
    patterns('',
             url(r'^$', CourseList.as_view(), name='index'),
             url(r'^c(?P<pk>\d+)$', CourseLastVersionRedirect.as_view(), name='course-last-version-redirect'),
             url(r'^d(?P<pk>\d+)$', CourseDetail.as_view(), name='course-detail'),
             url(r'^(?P<pk>\d+)$', CourseVersionDetail.as_view(), name='course-version-detail'),

             url(r'^c(?P<pk>\d+)-edit$', CourseUpdate.as_view(), name='course-edit'),
             url(r'^c(?P<pk>\d+)-delete$', CourseDelete.as_view(), name='course-delete'),
             url(r'^create$', CourseCreate.as_view(), name='course-create'),

             url(r'^v(?P<pk>\d+)-edit$', CourseVersionUpdate.as_view(), name='course-version-edit'),
    )
