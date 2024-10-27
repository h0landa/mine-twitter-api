from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from api.serializers import PostagemSerializer
from api.models import Postagem


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
