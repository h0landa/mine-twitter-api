from rest_framework import serializers
from api.models import UsuarioCustomizado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'password', 'foto_perfil',
                'perfil_verificado', 'foto_capa', 'bio',
                'data_aniversario']
        
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'perfil_verificado': {'required': False},
            'bio': {'required': False, 'allow_null': True},
            'foto_perfil': {'required': False, 'allow_null': True},
            'foto_capa': {'required': False, 'allow_null': True},
            'data_aniversario': {'required': False, 'allow_null': True},
        }

    def create(self, dados_validos):
        usuario = UsuarioCustomizado(**dados_validos)
        usuario.set_password(dados_validos['password'])
        usuario.save()
        return usuario
    
    def update(self, instance, dados_validos):
        instance.username = dados_validos.get('username', instance.username)
        instance.bio = dados_validos.get('bio', instance.bio)
        instance.foto_perfil = dados_validos.get('foto_perfil', instance.foto_perfil)
        instance.perfil_verificado = dados_validos.get('perfil_verificado', instance.perfil_verificado)
        instance.foto_capa = dados_validos.get('foto_capa', instance.foto_capa)
        instance.data_aniversario = dados_validos.get('data_aniversario', instance.data_aniversario)

        instance.save()
        return instance

    def validate(self, attrs):
        if self.context['request'].method == 'POST' and 'password' not in attrs:
            raise serializers.ValidationError({'password': 'Este campo é obrigatório.'})

        return attrs
