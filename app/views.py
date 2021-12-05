from django.http.response import JsonResponse
import datetime
from django.shortcuts import render
from app.classes import adminmail, mail

from app.models import Appointment, Image, Rate


def index(request):
    if request.method=="POST":
        print(datetime.date.today())
        DateAppointments=Appointment.objects.filter(Date=request.POST.get('Date'))
        print("TA",DateAppointments)
        for appoint in DateAppointments:
            if(appoint.Phone==request.POST.get('Phone')):
                print("true")
                return JsonResponse({"status": 'Appointment already Scheduled at '+request.POST.get('Date'),"status_code":1}) 
        print(request.POST.get('First_Name'))
        Appoint=Appointment()
        Appoint.First_Name=request.POST.get('First_Name')
        Appoint.Last_Name=request.POST.get('Last_Name')
        Appoint.Address=request.POST.get('Address')
        Appoint.Phone=request.POST.get('Phone')
        Appoint.Apt_Suite=request.POST.get('Apt_Suite')
        Appoint.Date=request.POST.get('Date')
        Appoint.Email=request.POST.get('Email')
        Appoint.save()
        mail("_mainaccount@satkar.online",Appoint.Email,"Appointment Scheduled",Appoint).start()
        adminmail("_mainaccount@satkar.online","memonayaj9864@gmail.com","Appointment Scheduled",Appoint).start()
        return JsonResponse({"status": 'Your appointment is Scheduled at '+request.POST.get('Date'),"status_code":0})

    return render(request,'index.html')

def faq(request):
    return render(request,'electrical-faq.html')


def rates(request):
    ratesset=Rate.objects.all()
    list=Rate._meta.fields
    # for l in list:
    #     print(str(l.name))

    dicts=dict()
    distincts=Rate.objects.order_by().values('Category').distinct()
    for dis in distincts:
        print(dis)
    cols=['Service_Name','Price']
    for dis in distincts:
        cats=Rate.objects.filter(Category=dis["Category"]).only('Service_Name','Category','Price')
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


def getimages(request):
    pagecount=int(request.GET.get('pagecount'))
    print(str(pagecount))
    offset=(pagecount-1)*12
    limit=pagecount*12
    # data=Image.objects.all()[0:5].values()
    images=list(Image.objects.all()[offset:limit].values())
    return JsonResponse(images,safe=False)

