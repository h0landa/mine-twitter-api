from rest_framework import generics, permissions, status
from rest_framework.response import Response
from api.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import UsuarioCustomizado, Seguidores
from api.serializers import SeguidoresSerializer

class RegistrarUsuarioView(generics.CreateAPIView):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class EditarUsuarioView(generics.UpdateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class VerPerfilUsuarioView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'usuario_id'

    def get_queryset(self):
        usuario_id = self.kwargs.get(self.lookup_url_kwarg)
        return UsuarioCustomizado.objects.filter(id=usuario_id)
    

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


class SeguirUsuarioView(generics.CreateAPIView):
    serializer_class = SeguidoresSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        usuario_seguidor = request.user
        usuario_seguido_id = request.data.get('usuario_seguido')
        
        if not usuario_seguido_id:
            return Response({"error": "O campo 'usuario_seguido' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        
        if Seguidores.objects.filter(usuario_seguidor=usuario_seguidor, usuario_seguido_id=usuario_seguido_id).exists():
            return Response({"detail": "Você já segue esse usuário."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(usuario_seguidor=usuario_seguidor)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)