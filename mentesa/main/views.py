from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages as message
from .services import PsicologoService, AgendamentoService

# Classe HomeView: responsável por exibir a página inicial
#################
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/home.html')


# Classe ListarPsicologosView: responsável por exibir a lista de psicólogos disponíveis
#############################
class ListarPsicologosView(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        psicologos = srv.recupera_psicologos()
        contexto = {'psis': psicologos}
        return render(request, 'main/psicologos.html', contexto)


# Classe DetalharPsicologoView: responsável por exibir os detalhes de um psicólogo específico
##############################
class DetalharPsicologoView(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        id = kwargs.get('psi_id')
        if not id:
            message.error(request, 'Identificador de psicólogo não fornecido.')
            return redirect('psicologos')
        contexto = srv.recupera_psicologo(id)
        if 'erro' in contexto:
            message.error(request, contexto['erro'])
            return redirect('psicologos')
        return render(request, 'main/agenda_psicologo.html', contexto)


# Classe AgendamentoView: responsável por lidar com o agendamento de consultas
########################
class AgendamentoView(View):
    def post(self, request, *args, **kwargs):
        srv = AgendamentoService()
        tipo = request.POST.get('tipo')
        id_horario = kwargs.get('id_h')
        if tipo and id_horario:
            contexto = srv.nova_consulta(tipo, id_horario, request.user)
        else:
            message.error(request, 'Dados do agendamento incompletos.')
            return redirect('psicologos')
        if 'erro' in contexto:
            message.error(request, contexto['erro'])
            return redirect('psicologos')
        return render(request, 'main/confirma_consulta.html', contexto)
    
    def get(self, request, *args, **kwargs):
        srv = AgendamentoService()
        id_horario = kwargs.get('id_h')
        retorno = srv.confirmar_consulta(id_horario, request.user)
        if 'status' in retorno and retorno['status'] == 'ok':
            message.success(request, 'Consulta agendada com sucesso!')
        else:            
            message.error(request, retorno.get('erro', 'Erro ao confirmar consulta.')) 
        return redirect('home')


# Classe BuscarPsicologoView: responsável por buscar psicólogos com base no nome fornecido
############################
class BuscarPsicologoView(View):
    def get(self, request, *args, **kwargs):
        srv = PsicologoService()
        nome = request.GET.get('nome')
        if not nome:
            message.error(request, 'Por favor, insira um nome para buscar.')
            return redirect('psicologos')
        psicologos = srv.buscar_psicologo(nome)
        contexto = {'psis': psicologos, 'consulta': 'nome com o texto: \'{}\''.format(nome)}
        return render(request, 'main/psicologos.html', contexto)
    

# Classe CancelarAgendamentoView: responsável por lidar com o cancelamento de agendamentos
################################
class CancelarAgendamentoView(View):
    def get(self, request, *args, **kwargs):
        srv = AgendamentoService()
        id_horario = kwargs.get('id_h')
        if not id_horario:
            message.error(request, 'Identificador de agendamento não fornecido.')
            return redirect('home')
        retorno = srv.cancelar_consulta(id_horario, request.user)
        if 'status' in retorno and retorno['status'] == 'ok':
            message.success(request, 'Consulta cancelada com sucesso!')
        else:
            message.error(request, retorno.get('erro', 'Erro ao cancelar consulta.'))
        return redirect('home')