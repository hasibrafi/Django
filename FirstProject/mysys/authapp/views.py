from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am Hasib Rafi.And I am from authapp/index.html"}
    return render(request,'authapp/index.html',context=my_dict)
    #return HttpResponse("Hello World")
