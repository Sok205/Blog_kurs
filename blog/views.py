from django.shortcuts import render
from .models import Post
# Create your views here.

def show_all_posts(request):
    """
    Return preview of all posts

    :param request:
    :return: render
    """
    feed = Post.objects.all()
    return render(request,"blog/feed.html",{"feed":feed})

