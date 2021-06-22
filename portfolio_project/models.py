from django.db import models
from django.contrib.auth.models import User 


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    body = models.TextField()
    link = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)



    
    

