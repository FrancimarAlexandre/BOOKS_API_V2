from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    DataNasc = models.DateField()

    def __str__(self):
        return self.nome

class Book(models.Model):
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    DataPub = models.DateField()
    DataCad = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Livro {self.titulo} do autor {self.autor}'
