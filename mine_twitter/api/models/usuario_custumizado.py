from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioCustumizado(AbstractUser):
    foto_perfil = models.ImageField(blank=True, null=True)
    perfil_verificado = models.BooleanField(default=False)
    foto_capa = models.ImageField(blank=True, null=True)
    bio = models.CharField(max_length=160)
    data_aniversario = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.username
    