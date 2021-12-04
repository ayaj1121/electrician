from datetime import datetime
from django.db import models
from django.db.models.enums import Choices
from django.conf import settings
import pytz
# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class RatesCategory(models.Model):
    Category = models.CharField(max_length=100)
    ModifiedAt=models.DateTimeField(default=datetime.now)
    CreatedAt=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Category
class Rate(models.Model):
    Service_Name= models.CharField(max_length=200)
    Pub_Date = models.DateTimeField(auto_now_add=True,blank=True)
    Price=models.IntegerField()
    Category=models.ForeignKey(RatesCategory,on_delete=models.DO_NOTHING,blank=True)
    ModifiedAt=models.DateTimeField(default=datetime.now)
    CreatedAt=models.DateTimeField(default=datetime.now)

class Image(models.Model):
    Image_Name=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Image=models.ImageField()
    ModifiedAt=models.DateTimeField(default=datetime.now)
    CreatedAt=models.DateTimeField(default=datetime.now)      



@receiver(pre_delete, sender=Image)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    print(instance.__dict__)
    instance.Image.delete(False)

class Appointment(models.Model):
    Phone=models.CharField(max_length=10,null=False,blank=False)
    First_Name=models.CharField(blank=False,max_length=30)
    Last_Name=models.CharField(blank=False,max_length=30)
    Address=models.CharField(blank=False,max_length=255)
    Apt_Suite=models.CharField(blank=False,null=False,max_length=255)
    Email=models.EmailField(blank=True)
    Date=models.DateField(blank=False)
    ModifiedAt=models.DateTimeField(default=datetime.now)
    CreatedAt=models.DateTimeField(default=datetime.now)