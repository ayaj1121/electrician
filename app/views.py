from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def faq(request):
    return render(request,'electrical-faq.html')


def rates(request):
    return render(request,'electrical-rates.html')

def contacts(request):
    return render(request,'electrical-contact.html')


def services(request):
    return render(request,'electrical-services.html')

def reviews(request):
    return render(request,'electrical-reviews.html')
