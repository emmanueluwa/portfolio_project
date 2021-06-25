from django.test import TestCase
import datetime 

from django.core.exceptions import ValidationError
from .factories import PortfolioFactory, TagFactory


from .models import Tag, Portfolio

class HomePageTests(TestCase):
    def SetUp(self):
        self.project = ProjectFactory()
        self.tag = TagFactory()


    def test_landing_on_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_context_data(self):
        response = self.client.get("/")
        context = response.context["projects"]
        self.assertEqual(list(context), list(Portfolio.objects.all()))
     


class ProjectPageTests(TestCase):
    def SetUp(self):
        pass

    def test_landing_on_projects_page(self):
        response = self.client.get("/projects")
        self.assertEqual(response.status_code, 200)


    def test_projects_context_data(self):
        response = self.client.get("/projects")
        context = response.context["projects"]
        self.assertEqual(list(context), list(Portfolio.objects.all()))
        

    
    