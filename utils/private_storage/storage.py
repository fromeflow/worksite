from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse_lazy
from django.core.files.storage import get_storage_class


class PrivateStorage(FileSystemStorage):
    def __init__(self):
        super().__init__(location=settings.PRIVATE_DIR)

    def url(self, name):
        return reverse_lazy('redirect-to-private', kwargs={'file_name': name})

private_storage = get_storage_class('utils.private_storage.storage.PrivateStorage')()