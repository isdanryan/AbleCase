from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect


# Create custom decorator to check the users role
def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return role_redirect(request.user.role)
        return _wrapped_view
    return decorator


def role_redirect(role):
    if role == 'Staff':
        return redirect('')
    elif role == 'Client':
        return redirect('/portal')
    else:
        raise PermissionDenied
