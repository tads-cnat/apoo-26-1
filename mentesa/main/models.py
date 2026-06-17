from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# CLASSE Paciente
#################
SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('o', 'Outro'),
)
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return f'Paciente: {self.user.first_name} {self.user.last_name}'


# CLASSE Especialidade
######################
class Especialidade(models.Model): 
    nome = models.CharField(max_length=50) 

    def __str__(self): 
        return self.nome  


# CLASSE Psicologo
##################
PRECO_PADRAO = 100.00  # Valor padrão para consultas, caso não haja preço específico definido
class Psicologo(models.Model):
    crp = models.CharField(max_length=10)
    nome = models.CharField(max_length=25)
    email = models.EmailField()
    especialidades = models.ManyToManyField(Especialidade)

    def __str__(self):
        return f'Psicólogo: {self.nome} - CRP: {self.crp}'
    def get_disponibilidades(self):
        disp = []
        for agenda in self.agenda_set.all():
            hoje = timezone.now().date()
            proximos = agenda.horario_set.filter(data__gte=hoje).filter(estado='d').order_by('data')[:15]
            disp.extend(proximos)
        return disp
    def get_preco(self, tipo):
        try:
            preco = self.precoconsulta_set.get(tipo=tipo)
            return preco.valor
        except PrecoConsulta.DoesNotExist:
            return PRECO_PADRAO  # Retorna o preço padrão se não houver preço específico para o tipo de consulta


# CLASSE PrecoConsulta
######################
TIPO_CONSULTA = (
    (1, 'Criança'),
    (2, 'Adulto'),
    (3, 'Casal'),
)    
class PrecoConsulta(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    tipo = models.IntegerField(choices=TIPO_CONSULTA)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.psicologo.nome}) Preço da Consulta: R${self.valor} - Tipo: {self.get_tipo_display()}'


# CLASSE Agenda
###############
class Agenda(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=25)

    def __str__(self):
        return f'Agenda: {self.nome} - Psicólogo: {self.psicologo.nome}'


# CLASSE Horario
################
ESTADO_HORARIO = (
    ('d', 'Disponível'),
    ('r', 'Reservado'),
    ('a', 'Agendado'),
)
class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=1, choices=ESTADO_HORARIO, default='d')

    def __str__(self):
        return f'Horário: {self.data} - {self.hora}'
    def reservar(self):
        self.estado = 'r'
        self.save()
    def agendar(self):
        self.estado = 'a'
        self.save()


# CLASSE Pagamento
##################
TIPO_PAGAMENTO = (
    (1, 'Cartão de Crédito'),
    (2, 'Cartão de Débito'),
    (3, 'Pix'),
)
class Pagamento(models.Model):
    tipo = models.IntegerField(choices=TIPO_PAGAMENTO, default=3)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'Pagamento: {self.get_tipo_display()} - R${self.valor}'


# CLASSE Consulta
#################
class Consulta(models.Model):
    tipo_consulta = models.IntegerField(choices=TIPO_CONSULTA)
    link_sala = models.URLField(blank=True, null=True)
    confirmada = models.BooleanField(default=False)
    realizada = models.BooleanField(default=False)
    presencial = models.BooleanField(default=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT)
    horario = models.OneToOneField(Horario, on_delete=models.RESTRICT)
    pagamento = models.OneToOneField(Pagamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Consulta: {self.get_tipo_consulta_display()} - Paciente: {self.paciente.user.first_name} {self.paciente.user.last_name} - Horário: {self.horario.data} {self.horario.hora}'
    def confirmar(self):
        self.horario.agendar()
        self.confirmada = True
        self.save()
