from django.conf.urls import patterns, url
from utils.private_storage.views import redirect_to_private

urlpatterns = [
    url(r'^(?P<file_name>.+)$', redirect_to_private, name='redirect-to-private')
]
