from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo
