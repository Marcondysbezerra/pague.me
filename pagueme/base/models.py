from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return self.nome
