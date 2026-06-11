from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages as message
from .services import PsicologoService, AgendamentoService

class Home(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        psicologos = srv.recupera_psicologos()
        contexto = {'psicologos': psicologos}
        return render(request, 'main/home.html', contexto)

class DetalharPsicologoView(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        id = kwargs['psicologo_id']
        contexto = srv.recupera_psicologo(id)
        return render(request, 'main/agenda_psicologo.html', contexto)
    
class AgendamentoView(View):
    def post(self, request, *args, **kwargs):
        srv = AgendamentoService()
        tipo = request.POST.get('tipo')
        id_horario = kwargs.get('id_h')
        consulta = srv.nova_consulta(tipo, id_horario, request.user)
        contexto = {'consulta': consulta}
        if consulta is None:
            message.error(request, 'Não foi possível iniciar o agendamento. Tente novamente.')
            return redirect('home')
        return render(request, 'main/confirma_consulta.html', contexto)
    
    def get(self, request, *args, **kwargs):
        srv = AgendamentoService()
        id_horario = kwargs.get('id_h')
        retorno = srv.confirmar_consulta(id_horario, request.user)
        if retorno == 'ok':
            message.success(request, 'Consulta agendada com sucesso!')
        else:            
            message.error(request, 'Não foi possível agendar a consulta.') 
        return redirect('home')
