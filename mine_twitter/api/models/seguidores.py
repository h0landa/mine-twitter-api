from django.db import models
from api.models import UsuarioCustomizado

class Seguidores(models.Model):
    usuario_seguidor = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE, related_name='seguidor')
    usuario_seguido = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE, related_name='seguindo')
    data_seguimento = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.usuario_seguidor.username} segue {self.usuario_seguido.username}'
