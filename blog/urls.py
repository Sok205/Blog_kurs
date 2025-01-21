from django.contrib import admin
from django.urls import path,include
from .views import show_all_posts, show_post, register_view, login_view, create_post, user_view

app_name = "posts"
urlpatterns = [
    # -----------------------------------------------------
    # Shows all posts. Used as the "Feed" page.
    # GET /feed/
    path("feed/", show_all_posts, name="feed"),

    # -----------------------------------------------------
    # Displays the same content as the feed, but at the root URL.
    # GET /
    path("", show_all_posts, name="home"),

    # -----------------------------------------------------
    # Displays the details for a single post identified by post_id.
    # e.g., GET /feed/42/
    path("feed/<post_id>/", show_post, name="details"),

    # -----------------------------------------------------
    # Shows a registration form and handles account creation.
    # GET /register/  (Display form)
    # POST /register/ (Process form submission)
    path("register/", register_view, name="register"),

    # -----------------------------------------------------
    # Shows a login form and handles user authentication.
    # GET /login/  (Display form)
    # POST /login/ (Process credentials)
    path("login/", login_view, name="login"),

    # -----------------------------------------------------
    # Displays a form to create a new post and handles submission.
    # GET /create_post/  (Display form)
    # POST /create_post/ (Process new post creation)
    path("create_post/", create_post, name="create_post"),

    # -----------------------------------------------------
    # Shows or manages a user’s profile or user-specific data.
    # GET /user_view/  (Display user info)
    # [Optionally POST /user_view/ if editing user data]
    path("user_view/", user_view, name="user_view"),
]