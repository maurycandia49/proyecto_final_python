from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_preview', 'fecha_nacimiento')
    search_fields = ('user__username', 'bio')
    readonly_fields = ('user',)
    
    fieldsets = (
        ('Usuario', {
            'fields': ('user',)
        }),
        ('Información Personal', {
            'fields': ('avatar', 'bio', 'fecha_nacimiento')
        }),
    )
    
    def bio_preview(self, obj):
        """Mostrar una vista previa de la biografía"""
        if obj.bio:
            return obj.bio[:50] + '...' if len(obj.bio) > 50 else obj.bio
        return '-'
    
    bio_preview.short_description = 'Biografía'

