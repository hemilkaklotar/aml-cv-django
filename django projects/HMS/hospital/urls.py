from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('admin_login/', login, name='login'),
    path('logout/', logout_admin, name='logout_admin'),
]