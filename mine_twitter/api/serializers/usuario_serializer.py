from rest_framework import serializers
from api.models import UsuarioCustomizado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['username', 'password', 'foto_perfil', 'perfil_verificado', 'foto_capa', 'bio', 'data_aniversario']
        extra_kwargs = {
            'password': {'write_only': True},
            'perfil_verificado': {'required': False},
            'bio': {'required': False, 'allow_null': True},
            'foto_perfil': {'required': False, 'allow_null': True},
            'foto_capa': {'required': False, 'allow_null': True},
            'data_aniversario': {'required': False, 'allow_null': True}
        }

    def create(self, dados_validos):
        usuario = UsuarioCustomizado(**dados_validos)
        usuario.set_password(dados_validos['password'])
        usuario.save()
        return usuario
