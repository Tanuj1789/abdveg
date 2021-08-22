from django.db import models

# Create your models here.
class Contact(models.Model):
    fname= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    desc= models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.fname