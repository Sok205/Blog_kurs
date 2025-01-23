from .views import gal_view
from django.urls import path,include

app_name = "galleries"

urlpatterns = [
    path("<gal>/", gal_view, name="gal_view"),
]