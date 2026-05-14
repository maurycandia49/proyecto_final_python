from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post


def home(request):
    """Vista de inicio del blog"""
    return render(request, 'home.html')


def about(request):
    """Vista de información sobre el autor"""
    return render(request, 'about.html')


def profile(request):
    """Vista de perfil de usuario"""
    return render(request, 'profile.html')


class PostListView(ListView):
    """Vista para listar todos los posts"""
    model = Post
    template_name = 'pages.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    """Vista para ver detalle de un post"""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Vista para crear un nuevo post"""
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'post_form.html'
    success_url = reverse_lazy('pages')
    success_message = "¡Post creado exitosamente!"
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Vista para editar un post existente"""
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'post_form.html'
    success_url = reverse_lazy('pages')
    success_message = "¡Post actualizado exitosamente!"
    login_url = 'login'


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Vista para eliminar un post"""
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('pages')
    success_message = "¡Post eliminado exitosamente!"
    login_url = 'login'
