from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'subtitulo', 'contenido')
    readonly_fields = ('fecha',)
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'subtitulo')
        }),
        ('Contenido', {
            'fields': ('contenido', 'imagen')
        }),
        ('Fecha', {
            'fields': ('fecha',),
            'classes': ('collapse',)
        }),
    )
