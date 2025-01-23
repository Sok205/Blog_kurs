from django.db import models
from PIL import Image

# Create your models here.

class Gal(models.Model):
    image_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "posts/%Y/%m/%d", null=True, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table = "gal"

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title
