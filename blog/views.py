from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.forms import ProfileForm
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save()

            # guardar datos del user
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()

            return redirect("profile")
    else:
        form = ProfileForm(instance=profile, initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        })

    return render(request, "edit_profile.html", {"form": form})
def profile(request):
    return render(request, 'profile.html')
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class PostListView(ListView):
    model = Post
    template_name = 'pages.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha']
    template_name = 'post_form.html'
    success_url = reverse_lazy('pages')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha']
    template_name = 'post_form.html'
    success_url = reverse_lazy('pages')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('pages')