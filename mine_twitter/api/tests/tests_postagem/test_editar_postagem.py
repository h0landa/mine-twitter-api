from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Postagem, Dispositivo


class EditarPostagensTests(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create_user(
            username='usuario_teste',
            password='senha-forte'
        )
        self.outro_usuario = UsuarioCustomizado.objects.create_user(
            username='outro_usuario_teste',
            password='outra-senha-forte'
        )

        self.dispositivo = Dispositivo.objects.create(
            nome_dispositivo='Android'
        )
        
        self.postagem = Postagem.objects.create(
            usuario=self.usuario,
            dispositivo=self.dispositivo,
            texto_postagem='Teste de postagem'
        )

        self.postagem_outro_usuario = Postagem.objects.create(
            usuario=self.outro_usuario,
            dispositivo=self.dispositivo,
            texto_postagem='Postagem de outro usuário'
        )

        resposta_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_teste',
            'password': 'senha-forte'
        })

        resposta_outro_usuario = self.client.post(reverse('token_obtain_pair'), {
            'username': 'outro_usuario_teste',
            'password': 'outra-senha-forte'
        })

        self.access_token_usuario = resposta_usuario.data['access']
        self.access_token_outro_usuario = resposta_outro_usuario.data['access']


    def test_usuario_pode_editar_sua_postagem(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
        self.client.login(username='usuario_teste', password='senha-forte')
        
        dados_atualizados = {'texto_postagem': 'Postagem atualizada'}

        response = self.client.patch(reverse('editar_postagem', kwargs={'postagem_id': self.postagem.id}), dados_atualizados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.postagem.refresh_from_db()
        self.assertEqual(self.postagem.texto_postagem, 'Postagem atualizada')


    def test_usuario_nao_pode_editar_postagem_de_outro_usuario(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_outro_usuario)
        self.client.login(username='outro_usuario_teste', password='outra-senha-forte')
        
        dados_atualizados = {'texto_postagem': 'Tentativa de edição'}

        resposta = self.client.patch(reverse('editar_postagem', kwargs={'postagem_id': self.postagem.id}), dados_atualizados)

        self.assertEqual(resposta.status_code, status.HTTP_403_FORBIDDEN)
