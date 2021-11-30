from email.message import EmailMessage
from smtplib import SMTP
import smtplib

# construct email
email = EmailMessage()
email['Subject'] = 'foo'
email['From'] = 'satkaron@satkar.online'
email['To'] = 'memonayaj9864@gmail.com'
email.set_content('<font color="red">red color text</font>', subtype='html')

# Send the message via local SMTP server.
with smtplib.SMTP_SSL('heimdall.protondns.net',465) as s:
    s.login('memonayaj@satkar.online','9[2f6Ikaa5L-JB')
    s.send_message(email)
