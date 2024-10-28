from rest_framework import serializers
from api.models import Seguidores, UsuarioCustomizado

class SeguidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'

        extra_kwargs = {
            'usuario_seguidor': {'required': False}
        }
        