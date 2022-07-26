import datetime
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image/')
    email = models.EmailField(max_length=150,blank=True,null=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    address = models.TextField(max_length=150,blank=True,null=True)
    created_date = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_date = models.DateTimeField(auto_now_add=True,blank=True,null=True )
    
