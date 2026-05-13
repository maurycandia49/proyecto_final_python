from django.urls import path
from .views import login_view, register_view, logout_view, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', edit_profile, name='edit_profile'),
     path("password-change/", auth_views.PasswordChangeView.as_view(
        template_name="password_change.html"
    ), name="password_change"),

    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="password_change_done.html"
    ), name="password_change_done"),
]