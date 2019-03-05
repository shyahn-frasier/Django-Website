from django.shortcuts import render
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
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})