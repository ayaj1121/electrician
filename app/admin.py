from django.contrib import admin
from app.models import Rates
from app.models import RatesCategory

# Register your models here.
class RatesAdmin(admin.ModelAdmin):
    list_display=('Service_Name','Pub_Date','Price','Category',)   


class RatesCategoryAdmin(admin.ModelAdmin):
    list_display=('Category','Pub_Date',)   

admin.site.register(Rates,RatesAdmin)
admin.site.register(RatesCategory,RatesCategoryAdmin)
