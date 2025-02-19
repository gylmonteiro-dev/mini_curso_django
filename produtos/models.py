from django.db import models

# Create your models here.
class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.FloatField()
    imagem = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.titulo