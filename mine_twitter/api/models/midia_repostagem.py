from django.db import models
from .repostagem import Repostagem


class Midia_Repostagem(models.Model):
    postagem = models.ForeignKey(Repostagem, on_delete=models.CASCADE)
    midia = models.TextField(blank=False, null=False)
