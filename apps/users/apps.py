from django.apps import AppConfig


class UsersAppDefaultConfig(AppConfig):
    """Default configuration for Users app."""
    name = 'apps.users'
    verbose_name = 'Users'

    # def ready(self):
    #     """Load signals and tasks on app ready"""
    #     from . import signals # noqa
    #     from . import tasks # noqa
