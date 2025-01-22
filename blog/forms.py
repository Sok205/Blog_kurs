from django import forms
from .models import Post


#Django will automatically create a form from provided model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title","content","image","status"]

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title","content","status"]



