from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Portfolio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.shortcuts import get_object_or_404, render




def home_page(request):
    projects = Portfolio.objects.all()[0:2]

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            data = {
                    'subject':subject,
                    'message': message,
                    'from_email': from_email
            }
            message = """ New message: {}  From: {}""". format(data['message'], data['from_email'])

            try:
                send_mail(data['subject'], message, '', ['fulonline1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.info(request, "Thank you, your message has been submitted. I will get back to you shortly.")
            return redirect('/')
               
    context = {'projects': projects, 'form':form }

    return render(request=request, template_name="home.html", context=context)



    
def projects_page(request):
    projects = Portfolio.objects.all()

    context = {'projects': projects}

    return render(request=request, template_name="projects.html", context=context)


def post_page(request, post_id):
    post = Portfolio.objects.get(id=post_id)
    context = {'post': post}
    return render(request, "post.html", context=context)
