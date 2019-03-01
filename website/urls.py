from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('games.html', views.games, name='games'),
    path('contact.html', views.contact, name='contact'),
]