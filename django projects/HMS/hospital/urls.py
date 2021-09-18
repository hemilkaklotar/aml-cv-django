from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

]