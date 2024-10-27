from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import UsuarioCustomizado

class DeletarUsuarioTests(APITestCase):
    def setUp(self):
        self.dados_usuario = {
            'username': 'usuario_teste',
            'password': 'senha_forte',
            'bio': 'Sou um usuario de teste.',
        }

        self.usuario = UsuarioCustomizado.objects.create_user(
            username = 'usuario_teste',
            password = 'senha_forte',
        )

        self.url = reverse('deletar_usuario', kwargs={'id': self.usuario.id})
        self.url_usuario_inexistente = reverse('deletar_usuario', kwargs={'id': '3'})

        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha_forte'
        })
        self.access_token = resposta.data['access']


    def test_deletar_usuario(self):
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
            resposta = self.client.delete(self.url)
            self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(UsuarioCustomizado.objects.filter(username='usuario_teste').exists())
    

    def test_deletar_usuario_inexistente(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        resposta = self.client.delete(self.url_usuario_inexistente)
        self.assertNotEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
