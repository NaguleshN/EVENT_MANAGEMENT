from django.shortcuts import render
from . models import *

def home(request):
  events=Event.objects.all()
  return render(request, 'core/home.html',{'events':events})

def login(request):
  return render(request, 'credential/login.html')

def add_event(request):
  if request.method =="POST":
    event_name=request.POST.get("event_name")
    instruction=request.POST.get("description")
    category=request.POST.get("category")
    date=request.POST.get("date")
    mode=request.POST.get("mode")
    registration_fee=request.POST.get("registration_fee")
    prize_amount=request.POST.get("prize")
    contact_number=request.POST.get("contact")
    time=request.POST.get("time")
    venue=request.POST.get("venue")
    Event.objects.create(event_name=event_name,instruction=instruction,category=category,date=date,mode=mode,registration_fee=registration_fee,prize_amount=prize_amount,contact_number=contact_number,time=time,venue=venue)

  return render(request, 'core/add_event.html')


def event_description(request,no):
  # events=Event.objects.all()
  event=Event.objects.get(id=no)
  return render(request,"core/event_description.html",{"event":event})