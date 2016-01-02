from django.conf.urls import patterns, url

from textbooks.views import *


urlpatterns = [
    url(r'^$', TextbookList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', TextbookDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)-edit$', TextbookUpdate.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)-delete$', TextbookDelete.as_view(), name='delete'),
    url(r'^create$', TextbookCreate.as_view(), name='create'),
]
