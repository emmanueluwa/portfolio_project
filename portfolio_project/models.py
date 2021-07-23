from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True, null=" ")
    description = models.CharField(max_length=150)
    body = RichTextField(blank=True, null=True)
    link = models.URLField(max_length=100, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(null=" ")

    def __str__(self):
        return self.title



  
        
    

