from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio

def home_page(request):
    projects = Portfolio.objects.all()

    context = {'projects': projects}

    return render(request, "home.html", context=context)



def projects_page(request):
    projects = Portfolio.objects.all()

    context = {'projects': projects}

    return render(request, "projects.html", context=context)
