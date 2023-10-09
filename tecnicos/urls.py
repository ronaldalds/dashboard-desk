from django.urls import path
from rest_framework import routers
from .views import Notificacao
from tecnicos.views import *

router = routers.DefaultRouter()
router.register(r'tecnico', TecnicosViewSet)
router.register(r'tipo', TiposOSViewSet)
router.register(r'sla', TempoSLAViewSet)
router.register(r'sla_os', SLA_OSViewSet)
router.register(r'mensagem', TecnicosMensagemViewSet)
router.register(r'informacao', InformacoesOSViewSet)

urlpatterns = [
    path('notificacao/iniciar/', Notificacao.as_view({'post': 'iniciar'}), name='iniciar_notificacao'),
    path('notificacao/start/', Notificacao.as_view({'post': 'start'}), name='iniciar_notificacao'),
    path('notificacao/parar/', Notificacao.as_view({'delete': 'parar'}), name='parar_notificacao'),
]

urlpatterns += router.urls