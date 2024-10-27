from rest_framework import generics, permissions, status
from rest_framework.response import Response
from api.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import UsuarioCustomizado


class RegistrarUsuarioView(generics.CreateAPIView):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class EditarUsuarioView(generics.UpdateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class AlterarSenhaView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioSerializer

    def update(self, request, *args, **kwargs):
        usuario = request.user
        dados_validos = {'password': request.data.get('password')}

        serializer = self.get_serializer(usuario, data=dados_validos, partial=True)
        serializer.is_valid(raise_exception=True)
        

        usuario.set_password(serializer.validated_data['password'])
        usuario.save()

        return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
    