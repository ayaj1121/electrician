import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import get_template
from django.conf import settings
settings.configure()
# me == my email address
# you == recipient's email address
me = "_mainaccount@satkar.online"
you = "memonayaj9864@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link to MB electrical"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html= """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

ctx = {
        'user': "Ajay"
    }
# html = get_template('mail_template.html').render(ctx)
 
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
    s.sendmail(me, you, msg.as_string())
    s.quit()
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
