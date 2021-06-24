from django.urls import path

from . import views

app_name = "portfolio_project"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("projects", views.projects_page, name="projects"),

]