from django.db import models
from usuario_custumizado import UsuarioCustumizado
from dispositivo import Dispositivo


class Postagem(models.Model):
    usuario = models.ForeignKey(UsuarioCustumizado, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.SET_NULL, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    texto_postagem = models.CharField(max_length=280)
    postagem_fixada = models.BooleanField(default=False)
    postagem_silenciada = models.BooleanField(default=False)


