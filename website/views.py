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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_info = form.save()
            contact_info.save()
            try:
                email = EmailMessage(contact_info,
                                    ['shyahn@321webmarketing.com'],
                                    )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})