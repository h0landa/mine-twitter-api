from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.views_usuario import RegistrarUsuarioView, EditarUsuarioView, AlterarSenhaView
from .views.views_dispositivos import CriarNovoDispositivoView, EditarDispositivoView, DeletarDispositivoView
from .views.views_postagem import CriarPostagemView, EditarPostagemView, DeletarPostagemView, CurtirPostagemView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registrar_usuario/', RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    path('editar_usuario/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('alterar_senha/', AlterarSenhaView.as_view(), name='alterar_senha'),

    path('criar_dispositivo/', CriarNovoDispositivoView.as_view(), name='criar_dispositivo_view'),
    path('editar_dispositivo/<int:dispositivo_id>', EditarDispositivoView.as_view(), name='editar_dispositvio'),
    path('deletar_dispositivo/<int:dispositivo_id>', DeletarDispositivoView.as_view(), name='deletar_dispositivo'),

    path('criar_postagem/', CriarPostagemView.as_view(), name='criar_postagem'),
    path('editar_postagem/<int:postagem_id>', EditarPostagemView.as_view(), name='editar_postagem'),
    path('deletar_postagem/<int:postagem_id>', DeletarPostagemView.as_view(), name='deletar_postagem'),
    path('curtir_postagem/', CurtirPostagemView.as_view(), name='curtir_postagem'),
]