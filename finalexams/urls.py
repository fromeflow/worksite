from django.conf.urls import patterns, url

from finalexams.views import FinalexamDetail, FinalexamListView

urlpatterns = patterns('',
                       url(r'^$', FinalexamListView.as_view(), name='finalexams-index'),
                       url(r'^(?P<finalexam_id>\d+)$', FinalexamDetail.as_view(),
                           name='finalexams-detail'),
)