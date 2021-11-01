from django.db import models

# Create your models here.
class Contact(modeLs,ModeL):
    email = modles.EmailField
    name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    feedback = models.TextField(max_length=350)

