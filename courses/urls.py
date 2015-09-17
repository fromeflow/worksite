from django.conf.urls import patterns, url

from .views import *


urlpatterns = \
    patterns('',
             url(r'^$', CourseList.as_view(), name='index'),
             url(r'^c(?P<pk>\d+)$', CourseLastVersionRedirect.as_view(), name='course-last-version-redirect'),
             url(r'^d(?P<pk>\d+)$', CourseDetail.as_view(), name='course-detail'),
             url(r'^(?P<pk>\d+)$', CourseVersionDetail.as_view(), name='course-version-detail'),
    )
