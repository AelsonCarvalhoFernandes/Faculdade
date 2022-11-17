from django.db import models

class Funcionarios(models.Model):
    nome = models.CharField(max_length=50, null=False)
    matricula = models.CharField(max_length=10, null=False)
    cargo = models.CharField(max_length=50, null=False)
    Salário = models.FloatField()

    def __str__(self):
        return self.nome
