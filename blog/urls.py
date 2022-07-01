from re import template
from django.urls import path
from . import views
from .views import (
    PostCreateView,
    PostListView, 
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView)
urlpatterns = [
    path('',views.landing,name='landing'),
    path('home/', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
]

