from django.apps import AppConfig


class TecnicosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tecnicos'

    def ready(self):
        from .util import NotificacaoTecnico
        from apscheduler.schedulers.background import BackgroundScheduler
        sheduler = BackgroundScheduler(daemon=True)
        notificacao = NotificacaoTecnico()
        notificacao.shedule_api()
        sheduler.configure(timezone="america/fortaleza")
        sheduler.add_job(notificacao.shedule_api, 'interval', minutes=10)

        sheduler.start()
