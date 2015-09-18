from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.utils.http import urlquote

@login_required
def redirect_to_private(request, file_name):
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename={file}"\
        .format(file=file_name)
    response['X-Accel-Redirect'] = urlquote("{private_internal_url}{file}"\
        .format(private_internal_url=settings.PRIVATE_INTERNAL_URL, file=file_name))
    return response
