from django.urls import path

from .views import (
    home,
    about,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', home, name='home'),

    path('about/', about, name='about'),

    path('pages/', PostListView.as_view(), name='pages'),

    path('pages/create/', PostCreateView.as_view(), name='create'),

    path('pages/<int:pk>/', PostDetailView.as_view(), name='detail'),

    path('pages/<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),

    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]