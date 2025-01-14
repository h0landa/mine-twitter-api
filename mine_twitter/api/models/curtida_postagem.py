from django.db import models
from .usuario_customizado import UsuarioCustomizado
from .postagem import Postagem


class CurtidaPostagem(models.Model):
    usuario = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)
