from django.contrib import admin
from .models import Paciente, Especialidade, Psicologo, PrecoConsulta, Agenda, Horario, Consulta, Pagamento

admin.site.site_header = "Mentesa Admin"
admin.site.site_title = "Administração - Clínica MenteSã"
admin.site.index_title = "Bem-vindo ao Portal de Administração da Clínica MenteSã" 

admin.site.register(Paciente)
admin.site.register(Especialidade)
admin.site.register(Psicologo)
admin.site.register(PrecoConsulta)
admin.site.register(Agenda)
admin.site.register(Horario)
admin.site.register(Consulta)
admin.site.register(Pagamento)