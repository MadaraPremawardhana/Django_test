from unittest import result
from urllib import request
from django.shortcuts import render
from datetime import datetime

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
