from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'courseworks.views.index'),
    url(r'^finished$', 'courseworks.views.finished'),
    url(r'^open$', 'courseworks.views.open'),
    url(r'^(?P<coursework_id>\d+)$', 'courseworks.views.detail'),
)