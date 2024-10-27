from rest_framework.test import APITestCase
from api.models import UsuarioCustomizado, Dispositivo, Postagem
from django.urls import reverse
from rest_framework import status


class DeletarPostagemTests(APITestCase):
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
        
        self.url_editar = reverse('editar_postagem', kwargs={'postagem_id': self.postagem.id})
        self.url_deletar = reverse('deletar_postagem', kwargs={'postagem_id': self.postagem.id})

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


    def test_usuario_pode_deletar_sua_postagem(self):
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
            self.client.login(username='usuario_teste', password='senha-forte')

            response = self.client.delete(reverse('deletar_postagem', kwargs={'postagem_id': self.postagem.id}))

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(Postagem.objects.filter(id=self.postagem.id).exists())


    def test_usuario_nao_pode_deletar_postagem_de_outro_usuario(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token_usuario)
        self.client.login(username='usuario_teste', password='senha-forte')

        url_outro_usuario = reverse('deletar_postagem', kwargs={'postagem_id': self.postagem_outro_usuario.id})

        response = self.client.delete(url_outro_usuario)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Postagem.objects.filter(id=self.postagem_outro_usuario.id).exists())
