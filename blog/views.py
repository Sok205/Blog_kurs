from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import PostForm
from django.core.paginator import Paginator
# Create your views here.


def show_all_posts(request):
    """
    Return preview of all posts

    :param request:
    :return: render
    """
    feed = Post.objects.filter(status="published")
    page_number = request.GET.get("page",1)
    per_page = request.GET.get("per_page",10)
    paginator = Paginator(feed, per_page)
    page_obj = paginator.page(page_number)
    return render(request,"blog/feed.html",{"page_obj":page_obj})

@login_required()
def show_post(request, post_id):
    """
    Return details of a single post
    If Post belongs to authenticated user he can update it. Form for updating is located in forms.py
    :param request:
    :param post_id
    :return:
    """
    post = None
    form_update = None
    post = get_object_or_404(Post, id = post_id, status ="published")
    if request.method == "POST":
        form_update = PostForm(request.POST, instance=post)
        if form_update.is_valid():
            form_update.save()

    if request.user == post.author:
        form_update = PostForm(instance=post)

    return render(request,"blog/details.html",{"post":post,"form_update":form_update})

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
    """
    return a create_post. It allows user to add posts if he is logged in
    :param request:
    :return:
    """
    if request.method == "POST":
        create_form = PostForm(request.POST)
        if create_form.is_valid():
            post = create_form.save(commit=False)
            post.author = request.user
            if request.user.is_superuser:
                post.status = "published"
            post.save()
        return redirect("posts:feed")
    else:
        create_form = PostForm()

    return render(request, "blog/create_post.html", {"create_form":create_form})


@login_required()
def user_view(request):
    """
    Creates a user_view where he can view his posts
    :param request:
    :return:
    """
    current_user = request.user
    user_id = current_user.id
    user_posts = Post.objects.filter(author = user_id)
    return render(request,"blog/user_view.html",{"user_posts":user_posts})

def user_logout(request):
    """
    Logs out the user
    :param request:
    :return:
    """
    logout(request)
    return redirect("posts:home")

