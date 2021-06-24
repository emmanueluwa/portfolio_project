from django.test import TestCase
import datetime 

from django.core.exceptions import ValidationError
from django.test import TestCase


from .models import Tag, Portfolio

class HomePageTests(TestCase):
    def SetUp(self):
        pass

    def test_landing_on_homepage(self):
      response = self.client.get("/")
      self.assertEqual(response.status_code, 200)



class ProjectsPageTests(TestCase):
    def SetUp(self):
        pass

    def test_landing_on_projects_page(self):
      response = self.client.get("/projects")
      self.assertEqual(response.status_code, 200)