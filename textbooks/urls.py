from django.conf.urls import patterns, url

from textbooks.views import *


urlpatterns = [
    url(r'^$', TextbookList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', TextbookDetail.as_view(), name='detail'),
]
