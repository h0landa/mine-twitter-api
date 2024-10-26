from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import UsuarioCustomizado

class UsuarioTests(APITestCase):
    def setUp(self):
        self.url = reverse('registrar_usuario')

        self.usuario_teste1 = UsuarioCustomizado.objects.create_user(
            username='usuario_teste1',
            password='senha_forte'
        )

        self.dados_usuario_teste1 = {
            'username': 'usuario_teste1',
            'password': 'senha_forte',
            'bio': 'Sou um usuario de teste.',
        }
        self.dados_usuario_teste2 = {
            'username': 'usuario_teste',
            'password': 'senha_forte',
            'bio': 'Este é um usuário de teste.',
        }

        self.client.post(self.url, self.dados_usuario_teste1)
        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste1',
            'password': 'senha_forte'
        })
        self.refresh_token = resposta.data['refresh']

    def test_registrar_usuario(self):
        resposta = self.client.post(self.url, self.dados_usuario_teste2)
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertTrue(UsuarioCustomizado.objects.filter(username='usuario_teste').exists())

    def test_registrar_usuario_com_username_existente(self):
        UsuarioCustomizado.objects.create_user(username='usuario_teste', password='senha_forte')
        resposta = self.client.post(self.url, self.dados_usuario_teste2)
        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_obtido(self):
        self.client.post(self.url, self.dados_usuario_teste2)
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
