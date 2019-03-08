from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage, send_mail
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
            subject = "Website Contact"
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['name'] and form. cleaned_data['number'] and form.cleaned_data['message']
            try:
                email = EmailMessage(subject, message, from_email, ['shyahn@321webmarketing.com'],)
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'website/contact.html', {'form': form})