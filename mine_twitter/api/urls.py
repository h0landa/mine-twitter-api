from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.views_usuario import RegistrarUsuarioView, EditarUsuarioView, AlterarSenhaView
from .views.views_usuario import SeguirUsuarioView, VerPerfilUsuarioView
from .views.views_dispositivos import CriarNovoDispositivoView, EditarDispositivoView, DeletarDispositivoView
from .views.views_postagem import EditarPostagemView, DeletarPostagemView
from .views.views_postagem import CurtirPostagemView
from .views.views_postagem import CriarPostagemView, VerPostagemView, FeedPostagensView



urlpatterns = [
    path('registrar_usuario/', RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    path('perfil_usuario/<int:usuario_id>', VerPerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('editar_usuario/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('alterar_senha/', AlterarSenhaView.as_view(), name='alterar_senha'),

    path('criar_dispositivo/', CriarNovoDispositivoView.as_view(), name='criar_dispositivo_view'),
    path('editar_dispositivo/<int:dispositivo_id>', EditarDispositivoView.as_view(), name='editar_dispositvio'),
    path('deletar_dispositivo/<int:dispositivo_id>', DeletarDispositivoView.as_view(), name='deletar_dispositivo'),

    path('criar_postagem/', CriarPostagemView.as_view(), name='criar_postagem'),
    path('postagem/<int:postagem_id>', VerPostagemView.as_view(), name='ver_postagem'),
    path('feed_postagens', FeedPostagensView.as_view(), name='postagens'),
    path('editar_postagem/<int:postagem_id>', EditarPostagemView.as_view(), name='editar_postagem'),
    path('deletar_postagem/<int:postagem_id>', DeletarPostagemView.as_view(), name='deletar_postagem'),

    path('curtir_postagem/', CurtirPostagemView.as_view(), name='curtir_postagem'),
    
    path('seguir_usuario/', SeguirUsuarioView.as_view(), name='seguir_usuario')

]