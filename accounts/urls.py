from django.conf.urls import patterns, url
import django.contrib.auth.views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
                       url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html'},
                           name='login'),
                       url(r'^logout$', auth_views.logout_then_login, {'login_url': reverse_lazy('accounts:login')},
                           name='logout'),
)
