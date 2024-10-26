from django.db import models
from usuario_custumizado import UsuarioCustumizado
from postagem import Postagem


class Mencao(models.Model):
    usuario_mencionado = models.ForeignKey(UsuarioCustumizado, on_delete=models.SET_NULL, null=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_mencao = models.DateTimeField(auto_now_add=True)
