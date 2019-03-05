from django.conf import settings
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
   