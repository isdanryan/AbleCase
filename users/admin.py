from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


# Set custom user admin area
class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ('email', 'user_name', 'first_name',
                    'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',
                           'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Personal', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name',
                       'password1', 'password2', 'is_staff', 'is_active',
                       'is_superuser', 'groups', 'user_permissions')}),
    )
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Users, CustomUserAdmin)
