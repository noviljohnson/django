# Create your views here.

# view function takes a request -> response
# request handler 
# action

# someting that user sees is template in django

# first view functio
from django.shortcuts import render
from django.http import HttpResponse

def cal():
    x = 1
    y = 2
    return x+y

def say_hello(request):
    # we can do
    # pull data from db
    # transform
    # send emails ... etc
    # now just return a simple response
    
    # return HttpResponse("Hello world")  # returning plane text

    # to run debugger    
    sm = cal()

    # return html response
    return render(request, 'hello.html', {'name':'Novil Johnson'})
