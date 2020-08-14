from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *
from random import randint
def index(request):
    confessions = Confession.objects.all()
    return render(request,"index.html",{"confessions":confessions[::-1]})

def new_confession(request):
    colors = ["yellow","blue","pink","green"]
    confession = request.GET.get("confession")
    color = colors[randint(0,3)]
    c = Confession(confession=confession,color=color)
    c.save()
    body = "{}".format(confession)
    email_msg = EmailMessage("New confession", body, settings.EMAIL_HOST_USER,
                             ["saswathcommand@gmail.com"])
    email_msg.send(fail_silently=False)
    return JsonResponse({"color":color},safe=False)