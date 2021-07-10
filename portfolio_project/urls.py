from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = "portfolio_project"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("projects", views.projects_page, name="projects"),
    path("post/<int:post_id>", views.post_page, name="post"),

    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/imges/favicon.ico'))
]

urlpatterns += staticfiles_urlpatterns()
