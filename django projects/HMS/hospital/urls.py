from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', index, name='dashboard'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', Delete_doctor, name='delete_doctor'),
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('view_patient/', View_patient, name='view_patient'),
    path('delete_patient(?P<int:pid>)/', Delete_patient, name='delete_patient'),
    path('add_patient/', Add_patient, name='add_patient'),
    path('view_appointment/', View_appointment, name='view_appointment'),
    path('delete_appointment(?P<int:pid>)/', Delete_appointment, name='delete_appointment'),
    path('add_appointment/', Add_appointment, name='add_appointment'),
]