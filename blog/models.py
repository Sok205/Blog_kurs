from django.db import models
from django.utils import timezone
from PIL import Image


class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.CharField(choices=STATUS_CHOICES, default = "draft", max_length = 10)
    posted_at = models.DateTimeField(blank = True, null = True)

    image = models.ImageField(upload_to = "posts/%Y/%m/%d", null=True, blank=True)

    class Meta:
        db_table = 'posts'

    def save(self, *args, **kwargs):
        if self.status == "published" and self.posted_at:
            self.posted_at = timezone.now()

        super().save(*args,**kwargs)


        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title
