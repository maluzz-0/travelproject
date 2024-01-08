from django.db import models

# Create your models here.
class reservation(models.Model):
    Name=models.CharField(max_length=20)
    EmailId=models.CharField(max_length=40)
    Guest=models.CharField(max_length=10)
    CheckInDate=models.DateField(max_length=10)
    Destination=models.CharField(max_length=20)
class adminlogin(models.Model):
    EmailId=models.CharField(max_length=50)
    Password=models.CharField(max_length=10)
