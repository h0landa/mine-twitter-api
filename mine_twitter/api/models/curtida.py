from django.db import models
from usuario_custumizado import UsuarioCustumizado
from postagem import Postagem


class Curtida(models.Model):
    usuario = models.ForeignKey(UsuarioCustumizado, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)
