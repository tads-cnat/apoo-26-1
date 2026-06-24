from .models import Psicologo, Consulta, Horario

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
    
    def confirmar_consulta(self, id_horario, usuario):
        try:
            horario = Horario.objects.get(pk=id_horario)
        except Horario.DoesNotExist:
            return {'erro': 'Identificador de horário inválido'}
        consulta = horario.consulta
        if consulta and hasattr(usuario, 'paciente'):
            consulta.confirmar()
            return {'status': 'ok'}
        return {'erro': 'Consulta não encontrada ou usuário não é um paciente.'}
    
    def cancelar_consulta(self, id_horario, usuario):
        try:
            horario = Horario.objects.get(pk=id_horario)
        except Horario.DoesNotExist:
            return {'erro': 'Identificador de horário inválido'}
        consulta = horario.consulta
        if consulta and hasattr(usuario, 'paciente'):
            consulta.cancelar()
            return {'status': 'ok'}
        return {'erro': 'Consulta não encontrada ou usuário não é um paciente.'}