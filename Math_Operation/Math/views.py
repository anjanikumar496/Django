from django.shortcuts import render

# Create your views here.

# pip install django-mathfilters

def Operations(request):
    return render(request,'math_operations.html')