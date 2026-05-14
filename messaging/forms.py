from django import forms
from .models import Mensaje, Conversacion


class MensajeForm(forms.ModelForm):
    """Formulario para enviar mensajes"""
    
    class Meta:
        model = Mensaje
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu mensaje...',
            }),
        }
        labels = {
            'contenido': 'Mensaje',
        }


class ConversacionForm(forms.ModelForm):
    """Formulario para crear una nueva conversación"""
    
    class Meta:
        model = Conversacion
        fields = []
