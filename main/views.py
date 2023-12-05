from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    prop = Products.objects.all()
    return render(request, 'main.html',{'prop':prop})

def about(request):
    return render(request,'about.html')