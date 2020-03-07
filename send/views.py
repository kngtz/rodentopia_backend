from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from .tasks import sleepy, send_email_task


def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT AGAIN</h1>')


# def index(request):
#     send_mail(
#         'This is the subject',
#         'hello this is an automated message',
#         'raggedcrowd',
#         ['meyal16532@mytrumail.com'],
#         fail_silently=False)

#     return render(request, 'send/index.html')
