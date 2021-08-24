from django.db import models
from django.http import request

# Create your models here.
class Contact(models.Model):
    fname= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    desc= models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.fname


class SellVeg(models.Model):
    email = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    addr= models.CharField(max_length=40)
    addr1= models.CharField(max_length=40)
    city= models.CharField(max_length=40)
    state= models.CharField(max_length=40)
    zip= models.CharField(max_length=40)
    def __str__(self):
        return self.name