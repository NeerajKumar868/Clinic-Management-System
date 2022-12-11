from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    patient_name=models.TextField(max_length=50)
    patient_age=models.IntegerField()
    patient_gender=models.TextField(max_length=10,blank=True)
    patient_location=models.TextField(max_length=50,blank=True )
    patient_date_of_visit=models.DateTimeField(auto_now_add=True)
    patient_reason_to_visit=models.TextField(max_length=25,blank=True )