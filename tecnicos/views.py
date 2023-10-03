from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework.views import APIView
from rest_framework.response import Response
from .util import NotificacaoTecnico
from rest_framework import status

ciclo = 60
sheduler = BackgroundScheduler(daemon=True)
notificacao = NotificacaoTecnico()
notificacao.shedule_api()
sheduler.configure(timezone="america/fortaleza")
sheduler.remove_all_jobs()
sheduler.add_job(notificacao.shedule_api, 'interval', minutes=ciclo, replace_existing=True)

sheduler.start()

class Notificacao(APIView):
    def post(self, request):
        global sheduler
        sheduler.configure(timezone="america/fortaleza")
        sheduler.remove_all_jobs()
        sheduler.add_job(notificacao.shedule_api, 'interval', minutes=ciclo, replace_existing=True)

        sheduler.start()
        return Response({"message": "Agendador iniciado"}, status=status.HTTP_200_OK)

    def delete(self, request):
        global sheduler
        print("aqui")
        sheduler.shutdown()
        return Response({"message": "Agendador parado"}, status=status.HTTP_200_OK)
