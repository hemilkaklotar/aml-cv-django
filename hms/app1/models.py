from django.db import models

class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True,max_length=10)
    admin_pass=models.CharField(default="",max_length=30)

class Book_App(models.Model):
    app_id=models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    patient_id=models.PositiveIntegerField()
    doc_id=models.PositiveIntegerField()
