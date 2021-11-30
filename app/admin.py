from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models import fields
from app.models import RatesCategory,Image,Appointment,Rate

# Register your models here.
@admin.register(Rate)
class RatesAdmin(admin.ModelAdmin):
    list_display=('Service_Name','Pub_Date','Price','Category',)   

@admin.register(RatesCategory)
class RatesCategoryAdmin(admin.ModelAdmin):
    list_display=('Category','Pub_Date',)   

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('Image_Name','Description','Image')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('Phone','First_Name','Last_Name','Address','Apt_Suite','Email')
    