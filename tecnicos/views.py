from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework.exceptions import MethodNotAllowed
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .util import NotificacaoTecnico
from rest_framework import status
from .serializer import *
from .models import *

ciclo = 60
sheduler = BackgroundScheduler(daemon=True)
notificacao = NotificacaoTecnico()
notificacao.shedule_api()
sheduler.configure(timezone="america/fortaleza")
sheduler.remove_all_jobs()
sheduler.add_job(notificacao.shedule_api, 'interval', minutes=ciclo, replace_existing=True)

sheduler.start()

class Notificacao(ViewSet):
    @swagger_auto_schema(
        operation_description="Get a list of objects.",
        responses={
            200: openapi.Response(
                description="Sucesso",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Reiniciar agendamento de notificação'),
                    },
                ),
            ),
            404: "Erro de Autenticação",
        }
    )
    def iniciar(self, request):
        global sheduler
        global notificacao
        sheduler.shutdown()
        notificacao.shedule_api()
        sheduler.configure(timezone="america/fortaleza")
        sheduler.remove_all_jobs()
        sheduler.add_job(notificacao.shedule_api, 'interval', minutes=ciclo, replace_existing=True)

        sheduler.start()
        return Response({"message": "Agendador iniciado"}, status=status.HTTP_200_OK)

    def parar(self, request):
        global sheduler
        print("aqui")
        sheduler.shutdown()
        return Response({"message": "Agendador parado"}, status=status.HTTP_200_OK)

class TecnicosViewSet(ModelViewSet):
    queryset = Tecnicos.objects.filter(status=True)
    serializer_class = TecnicosSerializer

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")


class TiposOSViewSet(ModelViewSet):
    queryset = TiposOS.objects.all()
    serializer_class = TiposOSSerializer


class TecnicosMensagemViewSet(ModelViewSet):
    queryset = TecnicosMensagem.objects.all()
    serializer_class = TecnicosMensagemSerializer


class TempoSLAViewSet(ModelViewSet):
    queryset = TempoSLA.objects.all()
    serializer_class = TempoSLASerializer


class SLA_OSViewSet(ModelViewSet):
    queryset = SLA_OS.objects.all()
    serializer_class = SLA_OSSerializer


class InformacoesOSViewSet(ModelViewSet):
    queryset = InformacoesOS.objects.all()
    serializer_class = InformacoesOSSerializer


class LogsViewSet(ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogsSerializer