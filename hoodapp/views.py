from django.shortcuts import render
import datetime as dt

# Create your views here.
def home(request):

  return render(request,'home.html')
