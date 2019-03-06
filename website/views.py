from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def games(request):
    return render(request, 'website/games.html', {})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            try:
                email = EmailMessage(name, phone, email, message,['shyahn@321webmarketing.com'],)
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'website/contact.html', {'form': form})