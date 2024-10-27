from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Postagem, Dispositivo

class CriarPostagemTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte'
        )
        self.dispositivo = Dispositivo.objects.create(
            nome_dispositivo='Iphone'
        )

        resposta_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })

        self.access_token_usuario = resposta_usuario.data['access']


    def test_criar_postagem(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
        self.client.login(username='usuario_teste', password='senha-forte')
        
        dados_postagem = {
            'dispositivo': self.dispositivo.id,
            'texto_postagem': 'uma postagem'
        }

        response = self.client.post(reverse('criar_postagem'), dados_postagem)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.postagem.refresh_from_db()
        self.assertTrue(Postagem.objects.filter(id=1).exists())

