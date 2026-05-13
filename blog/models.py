from django.db import models

class Post(models.Model):

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
