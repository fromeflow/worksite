from django.conf.urls import patterns, url


urlpatterns = \
    patterns('',
        url(r'^(?P<file_name>.+)$',
            'utils.private_storage.views.redirect_to_private',
            name='redirect-to-private')
    )
