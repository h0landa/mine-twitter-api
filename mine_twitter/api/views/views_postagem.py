from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from api.serializers import PostagemSerializer, CurtidaSerializer, MidiaPostagemSerializer
from api.models import Postagem, CurtidaPostagem, Seguidores
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from api.models import MidiaPostagem


class CriarPostagemView(generics.CreateAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]
    

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


class VerPostagemView(generics.RetrieveAPIView):
    serializer_class = PostagemSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'postagem_id'

    def get_queryset(self):
        postagem_id = self.kwargs.get(self.lookup_url_kwarg)
        return Postagem.objects.filter(id=postagem_id)

class CriarMidiaPostagemView(generics.CreateAPIView):
    queryset = MidiaPostagem.objects.all()
    serializer_class = MidiaPostagemSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

        curtida, created = CurtidaPostagem.objects.get_or_create(usuario=usuario, postagem=postagem)

        if created:
            return Response({'detail': 'Curtida adicionada.', 'data': CurtidaSerializer(curtida).data}, status=status.HTTP_201_CREATED)
        else:
            curtida.delete()
            return Response({'detail': 'Curtida removida.'}, status=status.HTTP_204_NO_CONTENT)


class FeedPostagensView(generics.ListAPIView):
    serializer_class = PostagemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuario_atual = self.request.user
        
        seguindo_ids = Seguidores.objects.filter(usuario_seguidor=usuario_atual).values_list('usuario_seguido', flat=True)

        return Postagem.objects.filter(usuario__in=seguindo_ids).order_by('-data_criacao') 