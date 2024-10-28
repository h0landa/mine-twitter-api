from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Postagem, Dispositivo


class VerPostagemTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte'
        )
        self.postagem = Postagem.objects.create(
            usuario=self.usuario,
            texto_postagem='Teste de postagem'
        )

        resposta_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })


        self.access_token_usuario = resposta_usuario.data['access']


    def test_ver_postagem(self):
        response = self.client.patch(reverse('postagem', kwargs={'postagem_id': self.postagem.id}))

        self.assertEqual(response.data['id'], self.postagem.id)
        self.assertEqual(response.data['texto_postagem'], 'Postagem original')
        self.assertEqual(response.data['usuario'], self.usuario.id)
