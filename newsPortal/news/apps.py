from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals
