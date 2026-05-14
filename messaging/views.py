from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Conversacion, Mensaje
from .forms import MensajeForm


@login_required
def inbox(request):
    """Vista del inbox con todas las conversaciones del usuario"""
    conversaciones = Conversacion.objects.filter(
        participantes=request.user
    ).prefetch_related('participantes', 'mensajes').order_by('-fecha_actualizacion')
    
    return render(request, 'messaging/inbox.html', {
        'conversaciones': conversaciones
    })


@login_required
def conversacion_detalle(request, pk):
    """Vista detalle de una conversación con sus mensajes"""
    conversacion = get_object_or_404(Conversacion, pk=pk, participantes=request.user)
    
    # Marcar mensajes como leídos
    Mensaje.objects.filter(
        conversacion=conversacion,
        remitente__in=[u for u in conversacion.participantes.all() if u != request.user],
        leido=False
    ).update(leido=True)
    
    mensajes = conversacion.mensajes.all()
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.conversacion = conversacion
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('conversacion_detalle', pk=pk)
    else:
        form = MensajeForm()
    
    otros_participantes = conversacion.participantes.exclude(id=request.user.id)
    
    return render(request, 'messaging/conversacion_detalle.html', {
        'conversacion': conversacion,
        'mensajes': mensajes,
        'form': form,
        'otros_participantes': otros_participantes,
    })


@login_required
def iniciar_conversacion(request, user_id):
    """Iniciar o ir a una conversación existente con un usuario"""
    otro_usuario = get_object_or_404(User, id=user_id)
    
    if otro_usuario == request.user:
        return redirect('inbox')
    
    # Buscar si ya existe una conversación entre los dos usuarios
    conversacion = Conversacion.objects.filter(
        participantes=request.user
    ).filter(participantes=otro_usuario).first()
    
    if not conversacion:
        # Crear nueva conversación
        conversacion = Conversacion.objects.create()
        conversacion.participantes.add(request.user, otro_usuario)
    
    return redirect('conversacion_detalle', pk=conversacion.pk)


@login_required
def nuevo_mensaje(request, user_id):
    """Crear un nuevo mensaje directo con un usuario"""
    otro_usuario = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            # Buscar o crear conversación
            conversacion = Conversacion.objects.filter(
                participantes=request.user
            ).filter(participantes=otro_usuario).first()
            
            if not conversacion:
                conversacion = Conversacion.objects.create()
                conversacion.participantes.add(request.user, otro_usuario)
            
            mensaje = form.save(commit=False)
            mensaje.conversacion = conversacion
            mensaje.remitente = request.user
            mensaje.save()
            
            return redirect('conversacion_detalle', pk=conversacion.pk)
    else:
        form = MensajeForm()
    
    return render(request, 'messaging/nuevo_mensaje.html', {
        'form': form,
        'destinatario': otro_usuario,
    })

