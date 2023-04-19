from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Festival, MyFestivalPlanning



# Create your views here.
def home(request):
    return render(request, 'home.html')

def festivals_index(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', { 'festival': festival})

def my_festivals_index(request):
    festivals = Festival.objects.filter(myfestivalplanning__user=request.user)
    return render(request, 'myfestivals/index.html', {'festivals': festivals})

def add_festival(request, festival_id):
    user = request.user
    festival = Festival.objects.get(id=festival_id)
    my_festivals_planning, created = MyFestivalPlanning.objects.get_or_create(user=user)
    my_festivals_planning.festivals.add(festival)
    return redirect('detail', festival_id=festival_id)
