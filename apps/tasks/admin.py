from django.contrib import admin

from apps.tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'modified',
    )
    readonly_fields = ('created', 'modified')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                (
                    'created',
                    'modified',
                )
            ),
        }),
    )

