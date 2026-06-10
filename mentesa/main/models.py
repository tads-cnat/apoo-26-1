from django.db import models

class Psicologo(models.Model):
    crp = models.CharField(max_length=10)
    nome = models.CharField(max_length=25)
    email = models.EmailField()
