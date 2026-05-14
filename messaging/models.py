from django.db import models
from django.contrib.auth.models import User


class Conversacion(models.Model):
    """Modelo para almacenar conversaciones entre usuarios"""
    participantes = models.ManyToManyField(User, related_name='conversaciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Conversación'
        verbose_name_plural = 'Conversaciones'
        ordering = ['-fecha_actualizacion']
    
    def __str__(self):
        participantes_str = ', '.join([u.username for u in self.participantes.all()])
        return f"Conversación: {participantes_str}"


class Mensaje(models.Model):
    """Modelo para almacenar mensajes dentro de una conversación"""
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['fecha_envio']
    
    def __str__(self):
        return f"Mensaje de {self.remitente.username} - {self.fecha_envio}"
