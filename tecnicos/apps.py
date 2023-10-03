from django.apps import AppConfig


class TecnicosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tecnicos'

    # def ready(self):
    #     from .views import start
    #     start()
