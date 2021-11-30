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

from app.models import Rate
import json


def index(request):
    if request.method=="POST":
        print(request.POST.get("First_Name"))
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
    mail("memonayaj@satkar.online","memonayaj9864@gmail.com","Thank you For you feedback").start()
    return render(request,'electrical-services.html')

def reviews(request):
    return render(request,'electrical-reviews.html')



class mail(Thread):
    def __init__(self,you,to,subject):
        self.you=you
        self.to=to
        self.subject=subject
        Thread.__init__(self)

    def run(self):
        # me == my email address
        # you == recipient's email address


        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.you
        msg['To'] = self.to
        ctx = {
                'user': "Ajay"
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
            s.login('memonayaj@satkar.online','9[2f6Ikaa5L-JB')
            s.sendmail(self.you, self.to, msg.as_string())
            s.quit()
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
