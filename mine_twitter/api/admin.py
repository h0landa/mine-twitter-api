from django.contrib import admin
from api.models import Dispositivo, UsuarioCustomizado, Postagem, CurtidaPostagem

admin.site.register(Dispositivo)
admin.site.register(UsuarioCustomizado)
admin.site.register(Postagem)
admin.site.register(CurtidaPostagem)
