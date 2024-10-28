from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Postagem, Dispositivo
from django.core.files.uploadedfile import SimpleUploadedFile


class CriarMidiaPostagem(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte'
        )
        self.dispositivo = Dispositivo.objects.create(
            nome_dispositivo='Iphone'
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


    def test_upload_midia(self):
        with open(r'C:\Users\usuario\Desktop\458370847_2885025691646239_7046391032785821844_n.jpg', 'rb') as file:
            upload_file = SimpleUploadedFile('testfile.jpg', file.read(), content_type='image/jpeg')
            dados_midia = {
                'midia': upload_file,
                'postagem': self.postagem.id
            }
            response = self.client.post(reverse('criar_midia_postagem'), dados_midia, format='multipart')
            
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertIn('midia', response.data)
