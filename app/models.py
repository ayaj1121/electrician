from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class RatesCategory(models.Model):
    Category = models.CharField(max_length=100)
    Pub_Date = models.DateTimeField(auto_now_add=True ,blank=True)


    def __str__(self):
        return self.Category
class Rate(models.Model):
    Service_Name= models.CharField(max_length=200)
    Pub_Date = models.DateTimeField(auto_now_add=True,blank=True)
    Price=models.IntegerField()
    Category=models.ForeignKey(RatesCategory,on_delete=models.DO_NOTHING,blank=True)

class Image(models.Model):
    Image_Name=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Image=models.ImageField()
        

class Appointment(models.Model):
    Phone=models.CharField(primary_key=True,max_length=10,null=False,blank=False)
    First_Name=models.CharField(blank=False,max_length=30)
    Last_Name=models.CharField(blank=False,max_length=30)
    Address=models.CharField(blank=False,max_length=255)
    Apt_Suite=models.CharField(blank=False,null=False,max_length=255)
    Email=models.EmailField(blank=True)