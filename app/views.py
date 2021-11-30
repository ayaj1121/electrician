from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import Rates
import json


def index(request):
    return render(request,'index.html')

def faq(request):
    return render(request,'electrical-faq.html')


def rates(request):
    ratesset=Rates.objects.all()
    list=Rates._meta.fields
    # for l in list:
    #     print(str(l.name))

    dicts=dict()
    distincts=Rates.objects.order_by().values('Category').distinct()
    for dis in distincts:
        print(dis)
    cols=['Service_Name','Price']
    for dis in distincts:
        cats=Rates.objects.filter(Category=dis["Category"]).only('Service_Name','Category','Price')
        for k in cats:
            print("key",k,"value")

        for cat in cats:
            print("type",type(cat))

            if str(cat.Category) in dicts.keys():
                print("second")
                dicts[str(cat.Category)].append(cat)
            else:
                print("first")
                dicts[str(cat.Category)]=[cat]
        
    # for rate in ratesset:
    #     print(rate.Service_Name)
    for k in dicts:
        print("keys",k,len(dicts[k]))
        for v in dicts[k]:
            print("values",)
    context={
        "dicts":dicts,
        "cols":cols
    }
    return render(request,'electrical-rates.html',context)

def contacts(request):
    return render(request,'electrical-contact.html')


def services(request):
    return render(request,'electrical-services.html')

def reviews(request):
    return render(request,'electrical-reviews.html')
