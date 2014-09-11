from django.conf.urls import patterns, url

from textbooks.views import TextbookDetail, TextbookListView

urlpatterns = \
    patterns('',
             url(r'^$', TextbookListView.as_view(), name='textbooks-index'),
             url(r'^(?P<textbook_id>\d+)$', TextbookDetail.as_view(), name='textbooks-detail'),
    )
