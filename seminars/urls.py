from django.conf.urls import patterns, url

from seminars.views import SeminarDetail

urlpatterns = \
    patterns('',
             # url(r'^$', 'seminars.views.index', name='seminars-index'),
             url(r'^(?P<seminar_id>\d+)$', SeminarDetail.as_view(), name='seminars-detail'),
             # url(r'^(?P<pk>\d+)-edit$', SeminarUpdate.as_view(), name='seminars-edit'),
             # url(r'^create$', SeminarCreate.as_view(), name='seminars-create'),
             # url(r'^(?P<pk>\d+)-delete$', SeminarDelete.as_view(), name='seminars-delete'),
    )
