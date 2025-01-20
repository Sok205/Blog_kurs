from django.contrib import admin
from django.urls import path,include
from .views import show_all_posts, show_post, register_view

app_name = "posts"
urlpatterns = [
    path("feed/",show_all_posts, name="feed"),
    path("feed/<post_id>/", show_post, name="details"),
    path("register/",register_view, name="register")
]