from xxsubtype import bench

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def show_all_posts(request):
    """
    Return preview of all posts

    :param request:
    :return: render
    """
    feed = Post.objects.filter(status="published")
    return render(request,"blog/feed.html",{"feed":feed})

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
            return redirect('posts:feed')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html",{"form":form})

def login_view(request):
    """
    ret
    :param request:
    :return:
    """
    pass

