from django.shortcuts import render

def home(request):
  return render(request, 'core/home.html')

def login(request):
  return render(request, 'credential/login.html')

def add_event(request):
  return render(request, 'core/add_event.html')