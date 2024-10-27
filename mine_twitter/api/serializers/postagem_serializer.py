from rest_framework import serializers
from api.models import Postagem, Curtida, Repostagem


class PostagemSerializer(serializers.ModelSerializer):
    quantidade_curtidas = serializers.SerializerMethodField()
    quantidade_repostagens = serializers.SerializerMethodField()
    
    class Meta:
        model = Postagem
        fields = ['id', 'usuario', 'dispositivo', 'texto_postagem',
                   'quantidade_curtidas', 'quantidade_repostagens']
        extra_kwargs = {
            'usuario': {'required': False},
        }
        
    def create(self, dados_validos):
        usuario = self.context['request'].user
        postagem = Postagem.objects.create(usuario=usuario, **dados_validos)
        return postagem
    
    def get_quantidade_curtidas(self, objeto_postagem):
        return Curtida.objects.filter(postagem=objeto_postagem).count()
    
    
    def get_quantidade_repostagens(self, objeto_postagem):
        return Repostagem.objects.filter(postagem=objeto_postagem).count()
