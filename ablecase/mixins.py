from django.core.exceptions import PermissionDenied


# Create custom mixin to check users role
class RoleRequiredMixin:
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.required_role and request.user.role != self.required_role:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    # What to do if user hasn't got the correct role
    def handle_no_permission(self):
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(self.request.get_full_path())