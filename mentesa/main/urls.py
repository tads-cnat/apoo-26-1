from django.urls import path
from .views import Home, DetalharPsicologoView, AgendamentoView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path(
        'psicologo/<int:psicologo_id>/', 
        DetalharPsicologoView.as_view(), name='detalhar_psicologo'),
    path(
        'horario/<int:id_h>/agendar/', 
        AgendamentoView.as_view(), name='agendar_consulta'),
]