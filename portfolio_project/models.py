from django.db import models
from django.contrib.auth.models import User 


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, null=" ")
    description = models.CharField(max_length=150)
    body = models.TextField()
    link = models.URLField(max_length=100, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    

    
    

