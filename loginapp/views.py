from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def create_account(request):
    return render(request, 'create.html')


def add_user(request):
    a1 = User()
    a1.first_name = request.POST.get('fname')
    a1.last_name = request.POST.get('lname')
    a1.email = request.POST.get('email')
    a1.username = request.POST.get('uname')
    password = request.POST.get('paswd')
    a1.set_password(password)
    a1.save()
    return redirect('/login')


def signup(request):
    username = request.POST.get('name')
    password = request.POST.get('passwd')
    b1 = authenticate(username=username,password=password)
    if b1 is not None and b1.is_superuser==1:
        return render(request,'admin.html')
    elif b1 is not None and b1.is_superuser==0:
        return render(request,'user.html')
    else:
        return HttpResponse('invald user')
