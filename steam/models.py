from django.db import models

class Game(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='images/')
    descrizione = models.TextField(max_length=100)
    prezzo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
