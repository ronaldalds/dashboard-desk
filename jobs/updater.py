from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import shedule_api


def start():
    sheduler = BackgroundScheduler(daemon=True)
    sheduler.configure(timezone="america/sao_paulo")
    sheduler.remove_all_jobs()
    sheduler.add_job(shedule_api, 'interval',
                     minutes=2, replace_existing=True)

    sheduler.start()
