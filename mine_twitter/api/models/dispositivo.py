from django.db import models


class Dispositivo(models.Model):
    nome_dispositivo = models.TextField()


    def __str__(self):
        return self.nome_dispositivo
