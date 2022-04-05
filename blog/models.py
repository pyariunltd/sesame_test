from unicodedata import category
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):

    blog_title = models.CharField(max_length=255)
    tags=TaggableManager()
    content=RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

