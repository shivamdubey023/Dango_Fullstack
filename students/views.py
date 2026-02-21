from django.shortcuts import render
from http import HttpResponse 



def students(request):
    return HttpResponse("Hello World")
