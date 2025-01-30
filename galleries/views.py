from xmlrpc.client import ResponseError

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Gallery, GalleryImage
from .forms import GalleryImageForm
# Create your views here.

def gallery_list(request):
    """
    Displays the gallery list
    :param request:
    :return:
    """
    galleries = Gallery.objects.all()
    return render(request, "galleries/list.html", {"galleries": galleries})

def img_details(request, id_id, img_id):
    """
    displays img_detail of image chosen from the gallery
    :param request:
    :param id_id:
    :param img_id:
    :return:
    """
    gallery = Gallery.objects.get(id=id_id)
    image = GalleryImage.objects.get(id=img_id)
    return render(request, "galleries/image_detail.html", {"image": image, "gallery": gallery})

def gallery_details(request, id_id):
    """
    displays the chosen gallery
    :param request:
    :param id_id:
    :return:
    """
    gallery = Gallery.objects.get(id=id_id)
    return render(request, "galleries/details.html", {"gallery": gallery})

def add_image_to_gallery(request, gallery_id):
    """
    adds image to gallery
    :param request:
    :param gallery_id:
    :return:
    """
    gallery = get_object_or_404(Gallery, id=gallery_id)

    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.gallery = gallery  # Force the correct gallery
            image.save()
            return redirect("galleries:list")
    else:
        form = GalleryImageForm()
    return render(request, "galleries/add_image_to_gallery.html", {"form": form, "gallery": gallery})



