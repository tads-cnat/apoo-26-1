from django.shortcuts import render
from django.views import View
from .services import PsicologoService

class PsicologoView(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        id = kwargs['id']
        contexto = srv.recupera_psicologo(id)
        return render(request, 'main/agenda_psicologo.html', contexto)
