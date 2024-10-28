from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Seguidores


class SeguirUsuarioTests(APITestCase):
    def setUp(self):
        self.usuario_seguidor = UsuarioCustomizado.objects.create_user(
            username='usuario_teste_seguidor',
            password='senha-forte'
        )

        self.usuario_seguido = UsuarioCustomizado.objects.create_user(
            username='usuario_teste_seguido',
            password='senha-forte'
        )


        resposta_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste_seguidor',
            'password': 'senha-forte'
        })


        self.access_token_usuario = resposta_usuario.data['access']


    def test_seguir_usuario(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
        self.client.login(username='usuario_teste_seguidor', password='senha-forte')

        dados_seguimento = {
            'usuario_seguido': self.usuario_seguido.id
        }
        response = self.client.post(reverse('seguir_usuario'), dados_seguimento)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Seguidores.objects.filter(usuario_seguido=self.usuario_seguido, usuario_seguidor=self.usuario_seguidor))
