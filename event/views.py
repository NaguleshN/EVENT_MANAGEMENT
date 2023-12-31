from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.shortcuts import render ,redirect
from . models import *
from django.contrib.auth import logout


def login(request):
  if request.method =="POST":
      print("hello")
      username=request.POST.get("username")
      password=request.POST.get("password")
      print(username,password)
      user=auth.authenticate(username=username,password=password)
      print(user)
      if user is not None:
          auth.login(request,user)
          return redirect('Home')
      else:
          return redirect('login')
  return render(request, 'credential/login.html')

@login_required(login_url='login')
def home(request):
  events=Event.objects.all()
  print(events)
  return render(request, 'core/home.html',{'events':events})

@login_required(login_url='login')
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

@login_required(login_url='login')
def event_description(request,no):
  # events=Event.objects.all()
  event=Event.objects.get(id=no)
  return render(request,"core/event_description.html",{"event":event})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")