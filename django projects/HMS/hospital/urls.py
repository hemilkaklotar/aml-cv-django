from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact')

]