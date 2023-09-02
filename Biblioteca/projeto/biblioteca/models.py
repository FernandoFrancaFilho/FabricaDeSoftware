from django.db import models

class Livro(models.Model):
    nome = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, blank=True, default='')
    preco = models.FloatField()

# Create your models here.
