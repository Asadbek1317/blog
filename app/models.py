from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=60)
    text = models.TextField()


class Register(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=60)