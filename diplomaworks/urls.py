from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'diplomaworks.views.index'),
    url(r'^open$', 'diplomaworks.views.open'),
    url(r'^(?P<diplomawork_id>\d+)$', 'diplomaworks.views.detail'),
)