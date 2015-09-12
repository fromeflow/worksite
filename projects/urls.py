from django.conf.urls import patterns, url

from projects.views import *


urlpatterns = \
    patterns('',
             # url(r'^$', CourseProjectList.as_view(), name='index'),
             # url(r'final^$', FinalProjectList.as_view(), name='final-index'),
             # url(r'open^$', OpenProjectList.as_view(), name='open-index'),
             # url(r'closed^$', OpenProjectList.as_view(), name='closed-index'),
             #
             # url(r'^create$', CourseProjectCreate.as_view(), name='create'),
             # url(r'^final-create$', FinalProjectCreate.as_view(), name='final-create'),

             url(r'^(?P<pk>\d+)$', CourseProjectDetail.as_view(), name='detail'),
             url(r'^final-(?P<pk>\d+)$', FinalProjectDetail.as_view(), name='final-detail'),
             # url(r'^(?P<pk>\d+)-edit$', ProjectUpdate.as_view(), name='edit'),
             # url(r'^(?P<pk>\d+)-delete$', ProjectDelete.as_view(), name='delete'),
    )
