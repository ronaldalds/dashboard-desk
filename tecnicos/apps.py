from django.apps import AppConfig


class TecnicosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tecnicos'

    def ready(self):
        from .util import Notificacao
        from apscheduler.schedulers.background import BackgroundScheduler
        sheduler = BackgroundScheduler(daemon=True)
        notificacao = Notificacao()
        sheduler.configure(timezone="america/fortaleza")
        sheduler.add_job(notificacao.shedule_api, 'interval', minutes=10)
        sheduler.add_job(notificacao.verificar_agenda_os, 'interval', minutes=15)

        sheduler.start()
