from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Destination
from accounts.models import Booking

# Create your views here.
def home(request):
    dest=Destination.objects.all()
    return render(request,'home.html',{'dests':dest})
def destination(request):
    image = request.GET.get('pic')
    dests=Destination.objects.all()
    for dest in dests:
        if dest.img.url==image:
            name=dest.dest_name
            price=dest.price
            desc=dest.desc    
    return render(request,'destination.html',{"image":image,'name':name,'price':price,'desc':desc})

def book(request):
    name = request.GET.get('name')
    dests=Destination.objects.all()
    user_id=request.user.id
    for dest in dests:
        if dest.dest_name==name:
            dest_id=dest.id
    book=Booking(user_id=user_id,dest_id=dest_id)
    book.save()
    return redirect('home')