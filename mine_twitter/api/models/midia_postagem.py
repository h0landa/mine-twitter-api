from django.db import models
from .postagem import Postagem


class Midia_Postagem(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    midia = models.TextField(blank=False, null=False)
