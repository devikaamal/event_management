from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if (p == cp):
            if User.objects.filter(username=u).exists():
                messages.info(request,"Username already exists...")
                return redirect('userapp:register')
            elif User.objects.filter(email=e).exists():
                messages.info(request, "Email id already exists...")
                return redirect('userapp:register')
            else:
                user = User.objects.create_user(username=u, email=e, password=p)
                user.save()
                messages.info(request, "Account Successfully Created...")
                return redirect('eventapp:home')

        else:
            messages.info(request, "Password Doesn't Match...")
            return redirect('userapp:register')

    return render(request, 'register.html')


def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            messages.info(request,"Login Success..")
            return redirect('eventapp:home')
        else:
            messages.info(request, "Invalid Credentials...")
            return redirect('userapp:register')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('eventapp:home')
