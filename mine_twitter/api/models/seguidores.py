from django.db import models
from mine_twitter.api.models.usuario_customizado import UsuarioCustumizado

class Seguidores(models.Model):
    usuario_seguidor = models.ForeignKey(UsuarioCustumizado, on_delete=models.CASCADE)
    usuario_seguido = models.ForeignKey(UsuarioCustumizado, on_delete=models.CASCADE)
    data_seguimento = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.usuario_seguidor.username} segue {self.usuario_seguido.username}'
