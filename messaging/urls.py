from django.urls import path
from .views import (
    inbox,
    conversacion_detalle,
    iniciar_conversacion,
    nuevo_mensaje,
)

app_name = 'messaging'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('conversacion/<int:pk>/', conversacion_detalle, name='conversacion_detalle'),
    path('iniciar/<int:user_id>/', iniciar_conversacion, name='iniciar_conversacion'),
    path('nuevo/<int:user_id>/', nuevo_mensaje, name='nuevo_mensaje'),
]
