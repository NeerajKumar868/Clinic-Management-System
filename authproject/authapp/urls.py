from turtle import home
from django.urls import path
from.views import *

urlpatterns=[
   path('index',homepage,name='homepage'),
   path("register", register_request, name="register"),
   path("login", login_request, name="login"),
   path("logout",logout_request, name= "logout"),
  
]