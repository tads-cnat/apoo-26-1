from .models import Psicologo, Consulta, Horario

# Classe PsicologoService: responsável por recuperar os psicólogos e suas disponibilidades
#########################
class PsicologoService():

    def recupera_psicologos(self):
        return Psicologo.objects.all()

    def recupera_psicologo(self, id):
        p1 = Psicologo.objects.get(pk=id)
        if p1:
            disp = p1.get_disponibilidades()
            return {'psicologo': p1, 'horarios': disp}
        return None
    
# Classe AgendamentoService: responsável por criar uma nova consulta
###########################
class AgendamentoService():

    def nova_consulta(self, tipo, id_horario, usuario):
        horario = Horario.objects.get(pk=id_horario)
        if horario and hasattr(usuario, 'paciente'):
            horario.reservar()
            consulta = Consulta(tipo_consulta=tipo, paciente=usuario.paciente, horario_id=id_horario)
            consulta.save()
            return consulta
        return None
    
    def confirmar_consulta(self, id_horario, usuario):
        horario = Horario.objects.get(pk=id_horario)
        consulta = horario.consulta
        if consulta and hasattr(usuario, 'paciente'):
            consulta.confirmar()
            return 'ok'
        return 'erro'