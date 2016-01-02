from django.conf.urls import patterns, url

from textbooks.views import *


urlpatterns = [
    url(r'^$', TextbookList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', TextbookDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)-edit$', TextbookUpdate.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)-delete$', TextbookDelete.as_view(), name='delete'),
    url(r'^create$', TextbookCreate.as_view(), name='create'),

    url(r'^(?P<pk>\d+)-add-file$', TextbookFileCreate.as_view(), name='file-add'),
    url(r'^file-(?P<pk>\d+)-edit$', TextbookFileUpdate.as_view(), name='file-edit'),
    url(r'^file-(?P<pk>\d+)-delete$', TextbookFileDelete.as_view(), name='file-delete'),
]
