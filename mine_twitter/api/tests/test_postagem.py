from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Postagem
from api.models import UsuarioCustomizado
from api.models import Dispositivo
from api.models import Seguidores


class PostagemAPITest(APITestCase):
    def setUp(self):
        self.usuario = UsuarioCustomizado.objects.create(
            username = 'usuario_teste',
            password = 'senha_forte',
        )
        self.usuario2 = UsuarioCustomizado.objects.create(
            username = 'usuario_teste2',
            password = 'senha_forte',
        )
        self.usuario3 = UsuarioCustomizado.objects.create(
            username = 'usuario_teste3',
            password = 'senha_forte',
        )
        self.dispositivo_android = Dispositivo.objects.create(
            nome_dispositivo = 'Android Teste'
        )
        self.dispositivo_iphone = Dispositivo.objects.create(
            nome_dispositivo = 'Iphone Teste'
        )

        self.seguidores = Seguidores.objects.create(
            seguidor = self.usuario,
            seguido = self.usuario2,
        )


        Postagem.objects.create(
            usuario=self.usuario,
            dispositivo=self.dispositivo_android,
            texto_postagem='Postagem do usuario'
        )
        Postagem.objects.create(
            usuario=self.usuario2,
            dispositivo=self.dispositivo_iphone,
            texto_postagem='Postagem do usuario2'
        )
        Postagem.objects.create(
            usuario=self.usuario3,
            dispositivo=self.dispositivo_iphone,
            texto_postagem='Postagem do usuario3'
        )

        self.url = '/pagina_principal/'
    

    def test_criar_postagem(self):
        dados = {
            'usuario': self.usuario.id,
            'dispositivo': self.dispositivo.id,
            'texto_postagem': 'Texto teste para postagem.'
        }
        resposta = self.client.post(self.url, dados)
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Postagem.objects.count(), 1)
        self.assertEqual(Postagem.objects.get().texto_postagem, 'Texto teste para postagem.')

    
    def test_listar_postagens_usuarios_seguindo(self):
        resposta = self.client.get(self.url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resposta.data), 1)
        self.assertEqual(resposta.data[0]['texto_postagem'], 'Postagem do usuario2')
    
    def test_obter_postagem_usuario(self):
        postagem = Postagem.objects.create(
            usuario=self.usuario,
            dispositivo=self.dispositivo,
            texto_postagem='Postagem para obter'
        )
        resposta = self.client.get(f'{postagem.usuario.username}/postagem/{postagem.id}')
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data['texto_postagem'], 'Postagem para obter')

    
    #def test_obter_postagem_inexistente(self):
        #resposta = self.client.get(f'{self.url}')