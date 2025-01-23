from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Gal
# Create your views here.

@login_required
def gal_view(request):
    user_id = request.user.id
    gallery = Gal.objects.filter(author = user_id)
    return render(request, "galleries/gal_view.html", {"gallery":gallery})