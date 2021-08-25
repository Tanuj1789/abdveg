from django.contrib import admin
from django.http import request
from django.urls import path,include
from mart import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("service",views.service, name="service"),
    path("contact",views.contact, name="contact"),
    path("login",views.login, name="login"),
    path("sellVeg",views.sellVeg, name="sellVeg"),
    path('productView/<int:pid>',views.productView, name="productView"),
    path('logout/', LogoutView.as_view()),

]
