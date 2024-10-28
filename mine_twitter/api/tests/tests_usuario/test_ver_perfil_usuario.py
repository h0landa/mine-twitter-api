from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Postagem, Dispositivo


class VerPerfilUsuarioTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte',
            bio='Uma bio teste'
        )


    def test_ver_perfil_usuario(self):
        response = self.client.get(reverse('perfil_usuario', kwargs={'usuario_id': self.usuario.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], self.usuario.bio)

