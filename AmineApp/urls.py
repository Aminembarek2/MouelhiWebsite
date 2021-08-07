from django.urls import path
from .views import  myhome, contact

urlpatterns = [
    path('',myhome,name="home"),
    path('contact/',contact,name="contact")
]