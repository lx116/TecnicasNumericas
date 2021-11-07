from django.shortcuts import render

# Create your views here.

def startApp(request):

    render(request,'base.html')