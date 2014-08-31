from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login$', 'account.views.login_view',
                           name='account-login'),
                       url(r'^logout$', 'account.views.logout_view',
                           name='account-logout'),
)
