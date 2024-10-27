from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers.usuario_serializer import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import UsuarioCustomizado

class RegistrarUsuarioView(generics.CreateAPIView):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class DeletarUsuarioView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioSerializer
    queryset = UsuarioCustomizado.objects.all()
    lookup_field = 'id'


