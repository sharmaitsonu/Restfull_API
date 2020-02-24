from django.db import models

# Create your models here.

class Employee(models.Model):
    full_name= models.CharField(max_length=20)
    empl_code= models.CharField(max_length=20)
    mobile= models.CharField(max_length=10)


