from django.db import models
from .usuario_customizado import UsuarioCustomizado
from .postagem import Postagem


class Mencao(models.Model):
    usuario_mencionado = models.ForeignKey(UsuarioCustomizado, on_delete=models.SET_NULL, null=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_mencao = models.DateTimeField(auto_now_add=True)
