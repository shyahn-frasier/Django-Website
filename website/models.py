from django.conf import settings
from django.db import models
from django.utils import timezone

class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Phone_Number(models.Model):
    number = models.CharField(max_length=100)

class Message(models.Model):
    message = models.TextField()