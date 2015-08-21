from django.conf.urls import patterns, url
import django.contrib.auth.views as auth_views

urlpatterns = patterns('',
                       url(r'^login$', auth_views.login, {'template_name': 'account/login.html'},
                           name='login'),
                       url(r'^logout$', 'account.views.logout_view',
                           name='logout'),
)
