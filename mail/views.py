from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import smtplib
def index(request):
    FROM = 'royalter24@gmail.com'
    TO = ['royalter24@gmail.com']
    SUBJECT = 'Done'
    TEXT = 'kukiiii'

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('royalter24@gmail.com', '0102Nole')
    server.sendmail(FROM, TO, message)
    server.close()

    return HttpResponse("mail sentfgd")
