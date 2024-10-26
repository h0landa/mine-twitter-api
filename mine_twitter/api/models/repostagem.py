from django.db import models
from postagem import Postagem
from usuario_custumizado import UsuarioCustumizado


class Repostagem(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UsuarioCustumizado, on_delete=models.CASCADE)
    repostagem = models.ForeignKey('self', on_delete=models.CASCADE)
    texto = models.CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return
