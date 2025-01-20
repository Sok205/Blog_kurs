from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import PostForm
# Create your views here.

@login_required()
def show_all_posts(request):
    """
    Return preview of all posts

    :param request:
    :return: render
    """
    feed = Post.objects.filter(status="published")
    return render(request,"blog/feed.html",{"feed":feed})

@login_required()
def show_post(request, post_id):
    """
    Return details of a single post
    :param request:
    :param post_id
    :return:
    """
    post = None
    post = get_object_or_404(Post, id = post_id, status ="published")
    return render(request,"blog/details.html",{"post":post})

def register_view(request):
    """
    TODO: Return two-step registration page for user

    Currently: Returns one-step registration page for user

    Function takes the POST method from register html and saves the provided user to user database

    IF POST then save user to database, else show empty form.

    Some sidenotes regarding the registration process:
    -Make sure that in <form action="{% url 'posts:register' %}" method="post"> correct path is provided, especially while using this path in urls
    -use csrf_token to ensure that your site is safe
    -correctly parse the form
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('posts:login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html",{"form":form})

def login_view(request):
    """
    Return a login view page from which a user can log in to his account

    Takes data from form located at /blog/login.html
    :param request:
    :return:
    """
    if request.method == "POST":
        log_form = AuthenticationForm(request,data = request.POST)
        if log_form.is_valid():
            login(request, log_form.get_user())
            return redirect("posts:feed")
    else:
        log_form = AuthenticationForm()

    return render(request,"blog/login.html",{"log_form":log_form})

@login_required()
def create_post(request):
    if request.method == "POST":
        create_form = PostForm(request.post)
        if create_form.is_valid():
            post = create_form.save(commit=False)
            post.author = request.user
            if request.user.is_superuser:
                post.status = "published"
            post.save()
        return redirect("blog:feed")
    else:
        create_form = PostForm()

    return render(request,"blog/new.html",{"create_form":create_form})


