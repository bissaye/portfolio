from django.shortcuts import render
from django.core.mail import send_mail
from .serializer import *
from .models import Messages
from .form import  *

# Create your views here.

def index(request):
    if request.method =='POST' :
        try:
            Messages.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message']
            )
            context={
                'message': "message sent successfully"
            }
            return render(request, 'blog/blog.html' , context)
        except:
            context={
                'message':"failed to send"
            }
            return render(request, 'blog/blog.html', context)
    else:
        context = {
            'message': " "
        }
        return render(request, 'blog/blog.html', context)
