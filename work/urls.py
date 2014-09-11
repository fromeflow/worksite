from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.shortcuts import render_to_response
from django.template import RequestContext

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^account/', include('account.urls')),
                       url(r'^courseworks/', include('courseworks.urls')),
                       url(r'^diplomaworks/', include('diplomaworks.urls')),
                       url(r'^finalexams/', include('finalexams.urls')),
                       url(r'^seminar/', include('seminars.urls')),
                       url(r'^student/', include('students.urls')),
                       url(r'^textbook/', include('textbooks.urls')),
                       # FIXME
                       url(r'^$', lambda r: render_to_response('base.html', context_instance=RequestContext(r)) ),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)