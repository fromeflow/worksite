from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'diplomaworks.views.index',
                           name='diplomaworks-index'),
                       url(r'^open$', 'diplomaworks.views.open',
                           name='diplomaworks-index-open'),
                       url(r'^(?P<diplomawork_id>\d+)$', 'diplomaworks.views.detail',
                           name='diplomaworks-detail'),
)