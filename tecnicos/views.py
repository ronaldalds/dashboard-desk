from rest_framework.exceptions import MethodNotAllowed
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *

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