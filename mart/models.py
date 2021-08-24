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
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    addr= models.CharField(max_length=20)
    addr1= models.CharField(max_length=20)
    city= models.CharField(max_length=20)
    state= models.CharField(max_length=20)
    zip= models.CharField(max_length=20)
    def __str__(self):
        return self.name