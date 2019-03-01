from django.shortcuts import render
from .forms import NameForm, PhoneNumberForm, MessageForm, ContactForm

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def games(request):
    return render(request, 'website/games.html', {})

def contact(request):
    #if request.method == "POST":
        #form = NameForm(request.POST)
       # if form.is_valid():
         #   name_info = form.save()
         #   name_info.save()
    #else:
     #   form = NameForm()

    #if request.method == "POST":
      #  form = PhoneNumberForm(request.POST)
       # if form.is_valid():
         #   phone_number_info = form.save()
          #  phone_number_info.save()
   # else:
     #   form = PhoneNumberForm()

   # if request.method == "POST":
      #  form = MessageForm(request.POST)
      #  if form.is_valid():
         #   message_info = form.save()
          #  message_info.save()
    #else:
       # form = MessageForm()

   if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_info = form.save()
            contact_info.save()
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})