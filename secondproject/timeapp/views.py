from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def tellmetime(request):
    time = datetime.datetime.now()
    return HttpResponse('<h1>time:'+str(time)+'<h1>')
