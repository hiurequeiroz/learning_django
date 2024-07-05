from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Cidade: {self.cidade}'
