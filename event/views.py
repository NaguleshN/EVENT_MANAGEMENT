from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.shortcuts import render ,redirect, get_object_or_404
from . models import *
from django.contrib.auth import logout
from .decorators import *


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
          return redirect('index')
      else:
          return redirect('login')
  return render(request, 'credential/login.html')

@login_required(login_url='login')
def home(request):
  events=AdminView.objects.all()
  print(events)
  return render(request, 'core/home.html',{'events':events})

@allowed_user(allowed_roles=['da', 'admin'])
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
    AdminView.objects.create(status="Pending",event_name=event_name,instruction=instruction,category=category,date=date,mode=mode,registration_fee=registration_fee,prize_amount=prize_amount,contact_number=contact_number,time=time,venue=venue)

  return render(request, 'core/add.html')

@login_required(login_url='login')
def event_description(request,no):
  event=Event.objects.get(id=no)
  return render(request,"core/event_description.html",{"event":event})


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")



@login_required
def index(request):
   events=AdminView.objects.all()
   return render(request, 'core/index.html', {'events': events, })



@login_required
def description(request, id):
   event = AdminView.objects.get(id = id)
   return render(request, 'core/description.html',{"event":event,})


@allowed_user(allowed_roles=['admin'])
@login_required
def admin(request):
   events = AdminView.objects.all()
   return render(request, 'admin_view/admin.html', {'events':events,})


@allowed_user(allowed_roles=['admin'])
def accept_order(request, order_id):
    order = get_object_or_404(AdminView, pk=order_id)
    order.status = 'accepted'
    order.save()
    return redirect('admin') 


@allowed_user(allowed_roles=['admin'])
def reject_order(request, order_id):
    order = get_object_or_404(AdminView, pk=order_id)
    order.status = 'rejected'
    order.delete()
    return redirect('admin') 

@allowed_user(allowed_roles=['admin'])
def accepted_event(request):
   events = AdminView.objects.all()
   return render(request, 'admin_view/accepted_events.html', {'events':events,})

def add_da_member(request):
   return render(request, 'admin_view/add_da_member.html')



