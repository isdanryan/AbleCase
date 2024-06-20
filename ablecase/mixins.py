from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


# Create custom mixin to check users role
class RoleRequiredMixin:
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.required_role and request.user.role != self.required_role:
            return self.role_redirect(request.user.role)
        return super().dispatch(request, *args, **kwargs)

    # What to do if user hasn't got the correct role
    def handle_no_permission(self, role=None):
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(self.request.get_full_path())

    # Custom redirect if the users role dosen't meet the requirements
    def role_redirect(self, role):
        if role == 'Staff':
            return redirect('')
        elif role == 'Client':
            return redirect('/portal')
        else:
            return self.handle_no_permission()
