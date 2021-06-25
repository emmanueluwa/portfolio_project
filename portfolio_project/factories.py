import datetime

import factory 
from django.contrib.auth.models import User

from . import models

class TagFactory(factory.django.DjangoModelFactory):
    name = "vue"



class PortfolioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Portfolio

    title = "building a cctv app"
    description = "steps used to buidl a cctv app with python"
    body = "xyz"
    tag = factory.SubFactory(TagFactory)

