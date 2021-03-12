from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Booking
from home.models import Destination

# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pass1=request.POST['password']

        user= auth.authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials...Try again")
            return redirect("login")
    else:
     return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2'] 

        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exists!!!! try another")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists!!!! try another")
                return redirect("register")
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save()
                messages.info(request,"user created successfully...please login")
                return redirect("login")
        else:
            messages.info(request,"Password mismatch!!!! try again")
            return redirect("register")
    else: 
     return render(request,'register.html')

def history(request):
    return render(request,'history.html')

def admin(request):
    return render(request,'admin.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

