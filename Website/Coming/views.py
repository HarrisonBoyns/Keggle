from django.conf.global_settings import EMAIL_HOST_USER
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ServerForm
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.

def coming(request):
    # if request.method == 'POST' and email and name:
    #     send_mail(subject="Enquiries", content="Sign Ip", settings.EMAIL_HOST_USER, ['kike1996@hotmail.com'], fail_silently=False)
    if request.method == 'GET':
        form = ServerForm()
    else:
        form = ServerForm(request.POST)
        if form.is_valid():
            subject = 'Important'
            email = form.cleaned_data['email']
            message =Mail(
                from_email='hitmebaby654321@gmail.com',
                to_emails='admin@learnhack.co.uk',
                subject=email,
                html_content='<strong>and easy to do anywhere, even with Python</strong>')

            try:
                # certificate = (os.environ.get('SENDGRID_API_KEY'))
                # sg = SendGridAPIClient(certificate)
                # sg.send(message)
                subject = 'Thank you for registering to our site'
                message = ' it  means a world to us '
                email_from = EMAIL_HOST_USER
                recipient_list = ['admin@learnhack.co.uk', ]
                send_mail(subject, message, email_from, recipient_list)
                # send_mail('Important', 'Here is the message.', 'hitmebaby654321@gmail.com', ['admin@learnhack.co.uk'],
                #           fail_silently=False)
                print('Working')
            except Exception as e:
                print(e)
            return render(request, "index.html", {'form': form})
    return render(request, "index.html", {'form': form})

def index(request):
    return HttpResponse("<h1>MyClub Event Calendar</h1>")

def successView(request):
    return HttpResponse('Success! Thank you for your message.')