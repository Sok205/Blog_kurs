from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Gallery, GalleryImage
# Create your views here.

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, "galleries/list.html", {"galleries": galleries})

def img_details(request, id, img_id):
    gallery = Gallery.objects.get(id=id)
    image = GalleryImage.objects.get(id=img_id)
    return render(request, "galleries/image_detail.html", {"image": image, "gallery": gallery})

def gallery_details(request, id):
    gallery = Gallery.objects.get(id=id)
    return render(request, "galleries/details.html", {"gallery": gallery})
