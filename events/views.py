from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event



def index(request):
    data ={
        "all_events": Event.objects.all()
    }
    return render(request,"event.htm",data)
     
