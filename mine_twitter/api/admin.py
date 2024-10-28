from django.contrib import admin
from api.models import Dispositivo, UsuarioCustomizado, Postagem, CurtidaPostagem
from api.models import MidiaPostagem


admin.site.register(Dispositivo)
admin.site.register(UsuarioCustomizado)
admin.site.register(Postagem)
admin.site.register(CurtidaPostagem)
admin.site.register(MidiaPostagem)
