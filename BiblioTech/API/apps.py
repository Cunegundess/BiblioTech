from django.apps import AppConfig


class BiblioapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'

    def ready(self):
        import API.signals
