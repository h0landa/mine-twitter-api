from rest_framework import serializers
from api.models import MidiaPostagem

class MidiaPostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MidiaPostagem
        fields = '__all__'

        extra_kwargs = {
            'postagem': {'required': True}
        }
        