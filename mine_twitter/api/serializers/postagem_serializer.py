from rest_framework import serializers
from api.models import Postagem, CurtidaPostagem, MidiaPostagem


class PostagemSerializer(serializers.ModelSerializer):
    quantidade_curtidas = serializers.SerializerMethodField()
    midias_postagem = serializers.SerializerMethodField()
    
    class Meta:
        model = Postagem
        fields = ['id', 'usuario', 'dispositivo', 'texto_postagem',
                   'quantidade_curtidas', 'midias_postagem']
        extra_kwargs = {
            'usuario': {'required': False},
        }
        
    def create(self, dados_validos):
        usuario = self.context['request'].user
        postagem = Postagem.objects.create(usuario=usuario, **dados_validos)
        return postagem
    
    def get_quantidade_curtidas(self, objeto_postagem):
        return CurtidaPostagem.objects.filter(postagem=objeto_postagem).count()
    

    def get_midias_postagem(self, objeto_postagem):
        return MidiaPostagem.objects.filter(postagem=objeto_postagem)
    
