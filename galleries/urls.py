from .views import gallery_list, gallery_details, img_details
from django.urls import path,include

app_name = "galleries"

urlpatterns = [
    path("", gallery_list, name="list"),
    path("<int:id_id>", gallery_details, name="details"),
    path("<int:id_id>/<img_id>/", img_details, name="img_details"),
]