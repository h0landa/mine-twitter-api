from rest_framework import serializers
from models import Postagem, Curtida, Repostagem


class PostagemSerializer(serializers.ModelSerializer):
    quantidade_curtidas = serializers.SerializerMethodField()
    quantidade_repostagens = serializers.SerializerMethodField()
    
    class Meta:
        model = Postagem
        fields = ['id', 'usuario', 'dispositivo', 'texto_postagem', 'quantidade_curtidas', 'quantidade_repostagens']

    
    def pegar_quantidade_curtidas(self, objeto_postagem):
        return Curtida.objects.filter(postagem=objeto_postagem).count()
    
    
    def pegar_quantidade_repostagens(self, objeto_postagem):
        return Repostagem.objects.filter(postagem=objeto_postagem).count()
