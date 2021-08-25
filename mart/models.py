from django.db import models
from django.http import request

# Create your models here.
class Contact(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    desc= models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.fname


class SellVeg(models.Model):
    email = models.TextField()
    name = models.TextField()
    price = models.TextField()
    addr= models.TextField()
    addr1= models.TextField()
    city= models.TextField()
    state= models.TextField()
    zip= models.TextField()
    def __str__(self):
        return str(self.id) + " " + self.name