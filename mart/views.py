from datetime import datetime
from django.shortcuts import render,HttpResponse
from mart.models import Contact,SellVeg
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

def sellVeg(request):
    current_user = request.user

    if current_user.id==None:
        return render(request,'../templates/login.html')
    else:
        if request.method == "POST":
            email= current_user.email
            # print(current_user.email)
            name= request.POST.get('name')
            price= request.POST.get('price')
            addr= request.POST.get('addr')
            addr1= request.POST.get('addr1')
            city= request.POST.get('city')
            state= request.POST.get('state')
            zip= request.POST.get('zip')
            sellveg= SellVeg(email=email,name=name,price=price,addr=addr,addr1=addr1,city=city,state=state,zip=zip)
            sellveg.save()
            messages.success(request, 'Your vegetables have been added!')
        return render(request,'../templates/sellVeg.html')

