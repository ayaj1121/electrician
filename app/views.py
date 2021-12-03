from django.http.response import JsonResponse
from django.utils import timezone
import datetime
from django.shortcuts import render
import smtplib
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread

from django.template.loader import get_template
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from django.core import serializers

from app.models import Appointment, Image, Rate
import json
import pytz

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

class mail(Thread):
    def __init__(self,you,to,subject,user):
        print("inside constructor")
        self.you=you
        self.to=to
        self.subject=subject    
        self.user=user
        Thread.__init__(self)

    def run(self):
        # me == my email address
        # you == recipient's email address

        print("inside run")
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.you
        msg['To'] = self.to
        ctx = {
                'user': self.user
            }
        html = get_template('mail_template.html').render(ctx)
        
        # Record the MIME types of both parts - text/plain and text/html.
        # part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        # msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        with smtplib.SMTP_SSL('heimdall.protondns.net',465) as s:
            s.login('_mainaccount@satkar.online','9[2f6Ikaa5L-JB')
            s.sendmail(self.you, self.to, msg.as_string())
            s.quit()
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
