from django.shortcuts import render ,HttpResponse
from django.http import HttpResponse
from django.views import generic
# Create your views here.
def home(request):
    return render(request,'home.html')
