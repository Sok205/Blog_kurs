from django.contrib import admin
from django.urls import path,include
from .views import show_all_posts
urlpatterns = [
    path("feed/",show_all_posts, name="feed"),
]