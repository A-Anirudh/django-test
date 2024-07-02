from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from .models import *

# Create your views here.

def home(request):
    return render(request, './home.html')

def date_view(request, year, month, day):
    now=datetime.now()
    birthday=datetime(year,month,day)
    current_datetime = datetime.now()
    year=datetime.now().year
    birthday=birthday.strftime('%Y-%m-%d')
    requested_date = datetime(year, month, day)
    if current_datetime>requested_date:
        requested_date = datetime(year+1, month, day)
        time_delta = current_datetime - requested_date
        days_difference = time_delta.days
    else:
    
        time_delta = current_datetime - requested_date
        days_difference = time_delta.days
     
    return HttpResponse(f'the birthday is {birthday} and the number of days left {abs(days_difference)}')