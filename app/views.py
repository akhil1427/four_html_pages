from django.shortcuts import render

# Create your views here.
def One(request):
    return render(request,'1.html')

def two(request):
    return render(request,'2.html')

def Third(request):
    return render(request,'3.html')

def Four(request):
    return render(request,'4.html')

