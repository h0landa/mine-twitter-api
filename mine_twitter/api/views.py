from rest_framework import generics, permissions
from .serializers.usuario_serializer import UsuarioSerializer
from api.models import UsuarioCustomizado

class UsuarioCreateView(generics.CreateAPIView):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]  # Permitir que qualquer um possa se registrar

