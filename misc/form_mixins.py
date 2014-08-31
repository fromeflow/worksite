from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy


class UserCheckMixin(object):
    user_check_failure_path = ''  # can be path, url name or reverse_lazy

    def check_user(self, user):
        return True

    def user_check_failed(self, request, *args, **kwargs):
        return redirect(self.user_check_failure_path)

    def dispatch(self, request, *args, **kwargs):
        if not self.check_user(request.user):
            return self.user_check_failed(request, *args, **kwargs)
        return super(UserCheckMixin, self).dispatch(request, *args, **kwargs)


class PermissionRequiredMixin(UserCheckMixin):
    user_check_failure_path = reverse_lazy('account-login')
    permission_required = None

    def check_user(self, user):
        return user.has_perm(self.permission_required)


class SuperuserRequiredMixin(UserCheckMixin):
    user_check_failure_path = reverse_lazy('account-login')

    def check_user(self, user):
        return user.is_superuser
