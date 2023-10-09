from rest_framework import routers
from tecnicos.views import *

router = routers.DefaultRouter()
router.register(r'tecnico', TecnicosViewSet)
router.register(r'tipo', TiposOSViewSet)
router.register(r'sla', TempoSLAViewSet)
router.register(r'sla_os', SLA_OSViewSet)
router.register(r'mensagem', TecnicosMensagemViewSet)
router.register(r'informacao', InformacoesOSViewSet)

urlpatterns = [
]

urlpatterns += router.urls