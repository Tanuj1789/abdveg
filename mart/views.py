from datetime import datetime
from django.shortcuts import render,HttpResponse
from mart.models import Contact
from datetime import datetime
from django.contrib import messages
import logging
# Create your views here.
def index(request):
    # context dictionary h
    context ={
        'variable': 'this is sent'
    }
    return render(request,'../templates/index.html')

def about(request):
    context ={
        'variable': 'this is sent'
    }
    return render(request,'../templates/about.html', context)

def service(request):
    context ={
        'variable': 'this is sent'
    }
    return render(request,'../templates/service.html', context)

def contact(request):
    if request.method == "POST":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email= request.POST.get('email')
        desc= request.POST.get('desc')
        contact= Contact(fname=fname, lname=lname, email=email, desc= desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you for the feedback!')
    return render(request,'../templates/contact.html')

def login(request):
    return render(request,'../templates/login.html')

