from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

# from django_object_actions import (
#     DjangoObjectActions,
#     takes_instance_or_queryset,
# )


from .models import User


@admin.register(User)
class UserAdmin(OriginalUserAdmin):
    """Admin panel for user model
    """
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_superuser',
        'last_login',
    )
    fieldsets = (
        (None, {
            'fields':
            (
                'username',
                'email',
                'password',
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
            'classes': ('collapse',),
        }),
    )

