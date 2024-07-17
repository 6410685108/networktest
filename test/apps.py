from django.apps import AppConfig


class TestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test'

    def ready(self):
        from .scheduler import start
        start()
