from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from api.serializers import DispositivoSerializer
from api.models import Dispositivo


class CriarNovoDispositivoView(generics.CreateAPIView):
    serializer_class = DispositivoSerializer
    permission_classes = [IsAdminUser]


class EditarDispositivoView(generics.UpdateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'dispositivo_id'

class DeletarDispositivoView(generics.DestroyAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'dispositivo_id'


