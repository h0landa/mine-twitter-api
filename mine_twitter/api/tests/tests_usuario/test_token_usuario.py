from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class UsuarioTokenTests(APITestCase):
    def setUp(self):
        self.url = reverse('registrar_usuario')

        self.dados_usuario = {
            'username': 'usuario_teste',
            'password': 'senha_forte',
            'bio': 'Sou um usuario de teste.',
        }

        self.client.post(self.url, self.dados_usuario)
        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha_forte'
        })
        self.refresh_token = resposta.data['refresh']


    def test_token_obtido(self):
        self.client.post(self.url, self.dados_usuario)
        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha_forte'
        })
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertIn('access', resposta.data)
        self.assertIn('refresh', resposta.data)

    def test_token_invalido(self):
        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_invalido',
            'password': 'senha_incorreta'
        })
        self.assertEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_refresh_token_valido(self):
        resposta = self.client.post(reverse('token_refresh'), {
            'refresh': self.refresh_token
        })
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertIn('access', resposta.data) 
