from django.urls import path
from .views import HomeView, DetalharPsicologoView, AgendamentoView
from .views import BuscarPsicologoView, ListarPsicologosView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'psicologos/', 
        ListarPsicologosView.as_view(), name='psicologos'),
    path(
        'psicologo/<int:psi_id>/', 
        DetalharPsicologoView.as_view(), name='detalhar_psicologo'),
    path(
        'psicologo/buscar/',
        BuscarPsicologoView.as_view(), name='buscar_psicologo'),
    path(
        'horario/<int:id_h>/agendar/', 
        AgendamentoView.as_view(), name='agendar_consulta'),
]