from unittest import result
from urllib import request
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect, render
from app1.forms import LogForm
from app1.models import LogMessage
import json

# Respond with "Hello, Django!" when the user requests the home page of the ap
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django!")

def hello1(request,name):
     content="Hello there,"+ name
     return HttpResponse(content)

def count_view(request,n):
    result = " "
    for i in range(1,int(n)+1):
        result += f"Hello {i} <br>"
    return HttpResponse(result)

def hello2(request, name):
    return render(request,'hello.html',
        {'name': name,'date': datetime.now()})

def hello3(request, firstname, lastname):
    return render(request,'hello_exercise1.html',
        {'firstname': firstname,'lastname':lastname, 'date': datetime.now()})

def count(request, number):
    arr=[]
    for i in range (int(number)):
        arr.append(i)
    return render(request,'count.html',{'arr_received':arr})

def home1(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

#######06/08/2024#####

def showMessages(request):
    messages=LogMessage.objects.order_by("-log_date")
    return render(request, "ShowMessages.html", {"message_list": messages})

def addMessage(request):
    form = LogForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save()
        return redirect("show")
        
    else:
        return render(request, "logMessage.html", {"form": form})

####AJAX BASED SEARCH###

def searchAjax(request,q):
    messagesList = LogMessage.objects.filter(message__contains=q)
    if(len(messagesList)>0):
        out="<table><tr><th>Date/Time</th><th>Title</th><th>Message</th><tr>"
        for x in messagesList:
            t = x.log_date.strftime("%A, %d %B, %Y at %X")
            out+="<tr><td>+t+</td><td>+x.title+</td><td>+x.message+</td></tr>"
            out+="</table>"
    else:
        out = "no matching results"
    return HttpResponse(out)