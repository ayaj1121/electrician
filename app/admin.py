from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models import fields
from app.models import RatesCategory,Image,Appointment,Rate

# Register your models here.
@admin.register(Rate)
class RatesAdmin(admin.ModelAdmin):
    list_display=('Service_Name','Pub_Date','Price','Category','CreatedAt','ModifiedAt')
    list_filter=('Pub_Date','Category','CreatedAt','ModifiedAt')
    search_fields = ("Service_Name", )
    exclude=('CreatedAt','ModifiedAt')   

@admin.register(RatesCategory)
class RatesCategoryAdmin(admin.ModelAdmin):
    list_display=('Category','CreatedAt','ModifiedAt')
    list_filter=('Category','CreatedAt','ModifiedAt')   
   
    exclude=('CreatedAt','ModifiedAt')   

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('Image_Name','Description','Image','CreatedAt','ModifiedAt')
    list_filter=('CreatedAt','ModifiedAt')
    exclude=('CreatedAt','ModifiedAt')   

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('Phone','First_Name','Last_Name','Address','Apt_Suite','Email','Date','CreatedAt','ModifiedAt')
    list_filter=('Phone','Email','Date','CreatedAt','ModifiedAt')
    exclude=('CreatedAt','ModifiedAt')   
