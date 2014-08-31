from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'courseworks.views.index',
                           name='courseworks-index'),
                       url(r'^finished$', 'courseworks.views.finished',
                           name='courseworks-index-finished'),
                       url(r'^open$', 'courseworks.views.open',
                           name='courseworks-index-open'),
                       url(r'^(?P<coursework_id>\d+)$', 'courseworks.views.detail',
                           name='courseworks-detail'),
)