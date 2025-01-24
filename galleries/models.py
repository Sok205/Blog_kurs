from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='galleries/%Y/%m/%d')
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.gallery.title