from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import UsuarioCustomizado

class RegistrarUsuarioTests(APITestCase):
    def setUp(self):
        self.url = reverse('registrar_usuario')

        self.dados_usuario = {
            'username': 'usuario_teste',
            'password': 'senha_forte',
            'bio': 'Sou um usuario de teste.',
        }


    def test_registrar_usuario(self):
        resposta = self.client.post(self.url, self.dados_usuario)
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertTrue(UsuarioCustomizado.objects.filter(username='usuario_teste').exists())


    def test_registrar_usuario_com_username_existente(self):
        UsuarioCustomizado.objects.create_user(username='usuario_teste', password='senha_forte')
        resposta = self.client.post(self.url, self.dados_usuario)
        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
