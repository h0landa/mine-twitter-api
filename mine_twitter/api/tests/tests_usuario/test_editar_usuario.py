from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado


class EditarUsuarioTest(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte',
        )
        self.url = reverse('editar_usuario')

        resposta = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })

        self.access_token = resposta.data['access']

    def test_editar_usuario(self):
        novos_dados = {
            'username': 'usuario_teste_novo',
            'bio': 'Nova biografia',
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.client.login(username='usuario_teste', password='senha-forte')
        resposta = self.client.patch(self.url, novos_dados)

        self.usuario.refresh_from_db()
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)

        self.assertEqual(self.usuario.username, 'usuario_teste_novo')
        self.assertEqual(self.usuario.bio, 'Nova biografia')

