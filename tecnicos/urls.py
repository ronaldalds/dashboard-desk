from django.urls import path
from .views import Notificacao

urlpatterns = [
    path('notificacao/', Notificacao.as_view()),
]