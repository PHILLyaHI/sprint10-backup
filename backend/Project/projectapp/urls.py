"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from projectapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("video/<int:pk>", VideoDetailView.as_view(), name="video-detail"),
    path("add_video/", AddVideoView.as_view(), name="add-video"),
    path('like/<int:pk>/', LikeView, name="like-video"),
    path("video/<int:pk>/comment", AddCommentView.as_view(), name="add-comment"),
    path('search_videos/', views.search_videos, name="search-videos"),
    path("user_list/", UserListView.as_view(), name="user-list"),
    path("email/", EmailView.as_view(), name="email"),
    path("video/<int:pk>/delete/", VideoDeleteView.as_view(), name="delte-video"),
]
