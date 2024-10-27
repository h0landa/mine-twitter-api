from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from api.serializers import PostagemSerializer, CurtidaSerializer
from api.models import Postagem, Curtida, UsuarioCustomizado


class CriarPostagemView(generics.CreateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class EditarPostagemView(generics.UpdateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'postagem_id'

    def get_object(self):
            postagem = super().get_object()
            
            if postagem.usuario != self.request.user:
                raise PermissionDenied("Você não tem permissão para editar esta postagem.")

            return postagem


    def perform_update(self, serializer):
        serializer.save()


class DeletarPostagemView(generics.DestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'postagem_id'

    def get_object(self):
            postagem = super().get_object()
            
            if postagem.usuario != self.request.user:
                raise PermissionDenied("Você não tem permissão para deletar esta postagem.")

            return postagem


    def perform_update(self, serializer):
        serializer.delete()


class CurtirPostagemView(generics.CreateAPIView):
    serializer_class = CurtidaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        usuario = request.user
        postagem_id = request.data.get('postagem')

        if not postagem_id:
            return Response({'detail': 'Postagem ID é necessário.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            postagem = Postagem.objects.get(id=postagem_id)
        except Postagem.DoesNotExist:
            return Response({'detail': 'Postagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        curtida, created = Curtida.objects.get_or_create(usuario=usuario, postagem=postagem)

        if created:
            return Response({'detail': 'Curtida adicionada.', 'data': CurtidaSerializer(curtida).data}, status=status.HTTP_201_CREATED)
        else:
            curtida.delete()
            return Response({'detail': 'Curtida removida.'}, status=status.HTTP_204_NO_CONTENT)

        