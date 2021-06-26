from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home_page(request):
    projects = Portfolio.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            try:
                send_mail(subject, message, "admin@example.com", ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
               
    context = {'projects': projects, 'form':form }

    return render(request, "home.html", context)



    
def projects_page(request):
    projects = Portfolio.objects.all()

    context = {'projects': projects}

    return render(request, "projects.html", context=context)


