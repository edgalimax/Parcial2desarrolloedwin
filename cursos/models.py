from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField(help_text="URL del video (YouTube/Vimeo, etc.)")
    descripcion = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} ({self.correo})"
