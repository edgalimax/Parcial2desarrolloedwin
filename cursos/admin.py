from django.contrib import admin
from .models import Video, Usuario

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'creado_en')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'fecha_registro')
