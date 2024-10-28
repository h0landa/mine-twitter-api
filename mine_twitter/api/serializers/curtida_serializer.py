from rest_framework import serializers
from api.models import CurtidaPostagem


class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurtidaPostagem
        fields = '__all__'

        extra_kwargs = {
            'usuario': {'required': False},
        }
    

    def create(self, dados_validos):
        usuario = self.context['request'].user
        curtida = CurtidaPostagem.objects.create(usuario=usuario, **dados_validos)
        return curtida