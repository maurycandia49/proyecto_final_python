
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm

from django.shortcuts import render, redirect
from .forms import ProfileForm

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

def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):

    if request.method == 'POST':

        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistroForm()

    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')