from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import user

def signup(request):
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f_name,l_name,username,email,password)
        if User.objects.filter(username=username).exists():
            print("SIC already used")
            messages.error(request,"SIC already used")
            return render(request,'user/signup.html')
        try:
            user = User.objects.create_user(
                 first_name=f_name,
                 last_name=l_name,
                 username=username,
                 email=email,
                 password=password
             )
            user.save()
            # print("user Created")
            messages.success(request,"Account Created Successfully.Please Log in ")
            return redirect('signin')
        except Exception as e:
            print(e)
            messages.error(request,e)
    return render(request,'user/signup.html')

def signin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('menu')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'user/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')