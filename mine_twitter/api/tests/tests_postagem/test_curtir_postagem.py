from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Curtida, UsuarioCustomizado, Postagem, Dispositivo


class CurtirPostagensTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte'
        )

        self.dispositivo = Dispositivo.objects.create(
            nome_dispositivo='Android'
        )

        self.postagem = Postagem.objects.create(
            usuario=self.usuario,
            dispositivo=self.dispositivo,
            texto_postagem='Teste de postagem'
        )

        resposta_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })

        self.access_token_usuario = resposta_usuario.data['access']

    def test_usuario_autenticado_curtir(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
        self.client.login(username='usuario_teste', password='senha-forte')


        dados_curtida = {
            'postagem': self.postagem.id
        }

        resposta = self.client.post(reverse('curtir_postagem'), dados_curtida)

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Curtida.objects.filter(usuario=self.usuario, postagem=self.postagem).exists())