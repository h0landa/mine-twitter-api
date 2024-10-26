from django.db import models
from .postagem import Postagem
from .usuario_customizado import UsuarioCustomizado


class Repostagem(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE)
    repostagem = models.ForeignKey('self', on_delete=models.CASCADE, related_name='repostagem_repostagem')
    texto = models.CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return
