from rest_framework import serializers
from api.models import Postagem, CurtidaPostagem


class PostagemSerializer(serializers.ModelSerializer):
    quantidade_curtidas = serializers.SerializerMethodField()
    
    class Meta:
        model = Postagem
        fields = ['id', 'usuario', 'dispositivo', 'texto_postagem',
                   'quantidade_curtidas']
        extra_kwargs = {
            'usuario': {'required': False},
        }
        
    def create(self, dados_validos):
        usuario = self.context['request'].user
        postagem = Postagem.objects.create(usuario=usuario, **dados_validos)
        return postagem
    
    def get_quantidade_curtidas(self, objeto_postagem):
        return CurtidaPostagem.objects.filter(postagem=objeto_postagem).count()
    
