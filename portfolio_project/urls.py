from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = "portfolio_project"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("projects", views.projects_page, name="projects"),
    path("post/<int:post_id>", views.post_page, name="post"),

]

urlpatterns += staticfiles_urlpatterns()