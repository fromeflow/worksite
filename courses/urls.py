from django.conf.urls import patterns, url

from .views import *


urlpatterns = \
    patterns('',
             url(r'^$', CourseList.as_view(), name='index'),
             url(r'^(?P<pk>\d+)$', CourseLastVersionDetail.as_view(), name='last-version-detail'),
             # url(r'^v(?P<pk>\d+)$', CourseVersionDetail.as_view(), name='course-version-detail'),
    )
