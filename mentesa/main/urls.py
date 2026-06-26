from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'psicologos/', 
        views.ListarPsicologosView.as_view(), name='psicologos'),
    path(
        'psicologo/<int:psi_id>/', 
        views.DetalharPsicologoView.as_view(), name='detalhar_psicologo'),
    path(
        'psicologo/buscar/',
        views.BuscarPsicologoView.as_view(), name='buscar_psicologo'),
    path(
        'horario/<int:id_h>/agendar/', 
        views.AgendamentoView.as_view(), name='agendar_consulta'),
    path(
        'horario/<int:id_h>/cancelar/',
        views.CancelarAgendamentoView.as_view(), name='cancelar_agendamento'),
    path(
        'agendamentos/avaliar',
        views.AvaliaAgendamentoView.as_view(), name='avalia_agendamentos'
    ),
]