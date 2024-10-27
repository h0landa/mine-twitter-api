from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado


class AlterarSenhaUsuarioTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte',
        )
        self.url = reverse('alterar_senha')

        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })
        self.access_token = resposta.data['access']

    def test_alterar_senha(self):
        nova_senha = {
            'password': 'senha-nova'
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.client.login(username='usuario_teste', password='senha-forte')
        resposta = self.client.patch(self.url, nova_senha)


        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data, {"detail": "Senha alterada com sucesso."})

    def test_alterar_senha_sem_autenticacao(self):
        nova_senha = 'nova_senha_forte123'
        response = self.client.patch(self.url, {'password': nova_senha})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
