from django.test import TestCase
import datetime 

from django.core.exceptions import ValidationError
from .factories import PortfolioFactory, TagFactory
from .forms import ContactForm


from .models import Tag, Portfolio

class HomePageTests(TestCase):
    def SetUp(self):
        self.portfolio = PortfolioFactory()
        self.tag = TagFactory()
        self.url = "/"
        

    def test_landing_on_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_context_data(self):
        response = self.client.get("/")
        context = response.context["projects"]
        self.assertEqual(list(context), list(Portfolio.objects.all()))
    

    def test_blank_contact_form(self):       #testing that there is a contact form on the homepage
        response = self.client.get("/")        
        context = response.context[0:2]

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(context, ContactForm)
        self.assertTemplateUsed(self.response, "/")
     

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


    
    