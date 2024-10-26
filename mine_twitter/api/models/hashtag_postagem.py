from django.db import models
from .hashtag import Hashtag
from .postagem import Postagem


class Hashtag_Postagem(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.SET_NULL, null=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
