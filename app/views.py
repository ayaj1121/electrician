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

    for dis in distincts:
        cats=Rates.objects.filter(Category=dis["Category"])
        for cat in cats:
            if cat in dicts.keys():
                dicts[str(cat.Category)].append(list(cat))
            else:
                dicts[cat.Category]=[cat]
            print(cat.Service_Name)
        
    # for rate in ratesset:
    #     print(rate.Service_Name)
    for k,v in dicts.keys():
        print(dicts[k])
    return render(request,'electrical-rates.html')

def contacts(request):
    return render(request,'electrical-contact.html')


def services(request):
    return render(request,'electrical-services.html')

def reviews(request):
    return render(request,'electrical-reviews.html')
