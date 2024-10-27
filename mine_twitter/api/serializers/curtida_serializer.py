from rest_framework import serializers
from api.models import Curtida


class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'

        extra_kwargs = {
            'usuario': {'required': False},
        }
    

    def create(self, dados_validos):
        usuario = self.context['request'].user
        curtida = Curtida.objects.create(usuario=usuario, **dados_validos)
        return curtida