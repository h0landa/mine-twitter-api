from django.db import models
from .postagem import Postagem


class MidiaPostagem(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    midia = models.ImageField(blank=False, null=False)
