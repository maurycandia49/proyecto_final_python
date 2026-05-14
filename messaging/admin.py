from django.contrib import admin
from .models import Conversacion, Mensaje


@admin.register(Conversacion)
class ConversacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'participantes_list', 'fecha_actualizacion', 'cantidad_mensajes')
    list_filter = ('fecha_creacion', 'fecha_actualizacion')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    fieldsets = (
        ('Participantes', {
            'fields': ('participantes',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    filter_horizontal = ('participantes',)
    
    def participantes_list(self, obj):
        """Mostrar lista de participantes"""
        return ', '.join([u.username for u in obj.participantes.all()])
    
    participantes_list.short_description = 'Participantes'
    
    def cantidad_mensajes(self, obj):
        """Mostrar cantidad de mensajes"""
        return obj.mensajes.count()
    
    cantidad_mensajes.short_description = 'Mensajes'


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'remitente', 'conversacion', 'fecha_envio', 'leido')
    list_filter = ('fecha_envio', 'leido')
    search_fields = ('contenido', 'remitente__username')
    readonly_fields = ('fecha_envio',)
    
    fieldsets = (
        ('Información del Mensaje', {
            'fields': ('conversacion', 'remitente', 'contenido')
        }),
        ('Estado', {
            'fields': ('leido', 'fecha_envio'),
            'classes': ('collapse',)
        }),
    )

