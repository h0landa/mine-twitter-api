from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrarUsuarioView, DeletarUsuarioView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registrar_usuario/', RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    path('deletar_usuario/<int:id>', DeletarUsuarioView.as_view(), name='deletar_usuario'),
]