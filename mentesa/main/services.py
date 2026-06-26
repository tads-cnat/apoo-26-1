from .models import Psicologo, Consulta, Horario
from abc import ABC, abstractmethod

# Classe PsicologoService: responsável por recuperar os psicólogos e suas disponibilidades
#########################
class PsicologoService():
    def recupera_psicologos(self):
        return Psicologo.objects.all()

    def recupera_psicologo(self, id):
        try:
            p1 = Psicologo.objects.get(pk=id)
        except Psicologo.DoesNotExist:
            return {'erro': 'Psicólogo não encontrado.'}
        if p1:
            disp = p1.get_disponibilidades()
            return {'psicologo': p1, 'horarios': disp}
    
    def buscar_psicologo(self, nome):
        return Psicologo.objects.filter(nome__icontains = nome)


# Classe AgendamentoService: responsável por criar uma nova consulta
###########################
class AgendamentoService():
    def nova_consulta(self, tipo, id_horario, usuario):
        try:
            horario = Horario.objects.get(pk=id_horario)
        except Horario.DoesNotExist:
            return {'erro': 'Identificador de horário inválido.'}
        if horario and hasattr(usuario, 'paciente'):
            horario.reservar()
            consulta = Consulta(tipo_consulta=tipo, paciente=usuario.paciente, horario=horario)
            consulta.save()
            preco = horario.agenda.psicologo.get_preco(tipo)
            return {'consulta': consulta, 'preco': preco} 
        return {'erro': 'Usuário logado não é um paciente.'}
    
    def agendar_consulta(self, id_horario, usuario):
        try:
            horario = Horario.objects.get(pk=id_horario)
        except Horario.DoesNotExist:
            return {'erro': 'Identificador de horário inválido'}
        consulta = horario.consulta
        if consulta and hasattr(usuario, 'paciente'):
            consulta.agendada()
            return {'status': 'ok'}
        return {'erro': 'Consulta não encontrada ou usuário não é um paciente.'}
    
    def cancelar_consulta(self, id_horario, usuario):
        try:
            horario = Horario.objects.get(pk=id_horario)
        except Horario.DoesNotExist:
            return {'erro': 'Identificador de horário inválido'}
        consulta = horario.consulta
        if consulta and hasattr(usuario, 'paciente'):
            consulta.cancelada()
            return {'status': 'ok'}
        return {'erro': 'Consulta não encontrada ou usuário não é um paciente.'}

# Classe ServiçoAgendamento
###########################
class ServicoAgendamento(ABC):
    @abstractmethod
    def get_nao_confirmados(user):
        pass
    @abstractmethod
    def confirma_agendamento(id_consulta, justificativa):
        pass

# Classe ImplServAgendamento
############################
class ImplServAgendamento(ServicoAgendamento):
    def get_nao_confirmados(self, user):
        if hasattr(user, 'psicologo'):
            lista = Consulta.objects.filter(estado=1, horario__agenda__psicologo=user.psicologo)
            return {'lista': lista}
        return {'erro': 'Usuário informado não é psicologo'}
    def confirma_agendamento(self, id_consulta, justificativa):
        try:
            consulta = Consulta.objects.get(pk=id_consulta)
            consulta.confirmada()
            return {'sucesso': 'Consulta confirmada com sucesso!'}
        except Consulta.DoesNotExist:
            return {'erro': 'Identificador de consulta inválido!'}


# Classe FabricaServicos
########################
class FabricaServicos(ABC):
    @staticmethod
    def servico_agendamento() -> ServicoAgendamento:
        srv = ImplServAgendamento()
        return srv