from django.shortcuts import render,redirect
from django.shortcuts import render
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
    i=0
    j=0
    dic=list()
    book_dests=list()
    books_id=list()
    dests2=list()
    user_id=request.user.id
    books=Booking.objects.all()
    dests=Destination.objects.all()
    users=User.objects.all()
    for user in users:
        if user.id==user_id:
            fname=user.username
    if Booking.objects.filter(user_id=request.user.id).exists():
        for book in books:
            if book.user_id==user_id:
                books_id.append(book.id)
                book_dests.append(book.dest_id)
                for i in range(len(books_id)):
                    for dest in dests:
                        if dest.id==book_dests[i]:
                            if dest.dest_name not in dests2:
                             dests2.append(dest.dest_name)   
    else:
        messages.info(request,"no history available for you with Travello.")
        return redirect("/")
    
    for j in range(len(dests2)):
        id1=books_id[j]
        name=dests2[j]
        dic.append({"id":id1,"name":name}.values())
    return render(None,'history.html',{"name":fname,'dests':dic})

def admin(request):
    user=User.objects.filter(id=request.user.id)
    for x in user:
        user1=x
    return render(request,'admin.html',{'name':user1})

def logout(request):
    auth.logout(request)
    return redirect("/")

def add(request):
    return redirect("admin")

def modify(request):
    return redirect("admin")

def show(request):
    dic=list()
    users=User.objects.all()
    for user in users:
        dic.append({'id':user.id,'uname':user.username,'fname':user.first_name,'lname':user.last_name,'email':user.email,'passwor':user.password}.values())   
    return render(request,"show.html",{'users':dic})

def showbook(request):
    dic=list()
    users=User.objects.all()
    
    for user in users:
        dic.append({'id':user.id,'uname':user.username,'fname':user.first_name,'lname':user.last_name,'email':user.email,'passwor':user.password}.values())   
    return render(request,"show.html",{'users':dic})

