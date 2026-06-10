from .models import Psicologo

class PsicologoService():
    def recupera_psicologo(self, id):
        p1 = Psicologo.objects.get(pk=id)
        disp = p1.get_disponibilidades()
        return {'psicologo': p1, 'horarios': disp}